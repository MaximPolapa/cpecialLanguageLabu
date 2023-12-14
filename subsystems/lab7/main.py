import requests
import json
import csv
import re
import logging
from prettytable import PrettyTable
import prettytable



logging.basicConfig(filename='library_service.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class APIClient:
    def __init__(self):
        self.api_url = 'https://jsonplaceholder.typicode.com/posts'  # Прикладний URL для API

    def get_books(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error during API request: {e}")
            return None

    def list_books(self):
        books = self.get_books()
        return books if books else []
    
    def add_book(self, data):
        try:
            response = requests.post(self.api_url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error during API request: {e}")
            return None

    def search_books(self, keyword, search_by='title'):
        books = self.get_books()
        if books:
            return [book for book in books if keyword.lower() in book[search_by].lower()]
        return []

class Library:
    def __init__(self, client):
        self.client = client

    def list_books(self):
        return self.client.get_books()

    def add_book(self, title, author):
        book_data = {'title': title, 'author': author}
        return self.client.add_book(book_data)

    def search_books(self, title):
        return self.client.search_books(title)

class DataHandler:
    @staticmethod
    def save_data(data, format_type):
        if format_type == 'json':
            with open('books.json', 'w') as f:
                json.dump(data, f, indent=4)
        elif format_type == 'csv':
            with open('books.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        elif format_type == 'txt':
            with open('books.txt', 'w') as f:
                f.write(str(data))

class UI:
    def __init__(self, library):
        self.library = library

    def run(self):
        while True:
            print("\nOptions:")
            print("1. List all books")
            print("2. Add a book")
            print("3. Search book by title")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                books = self.library.list_books()
                if books:
                    table = PrettyTable()
                    table.field_names = ["ID", "Title", "Body"]
                    table.max_width = 30
                    table.align["Title"] = "l"
                    table.align["Body"] = "l"
                    table.border = True
                    table.hrules = prettytable.ALL

                    for book in books:
                        table.add_row([book['id'], book['title'], book['body']])
                    print(table)

                    # Запитуємо у користувача, чи хоче він зберегти дані
                    save_choice = input("Would you like to save these books to a text file? (yes/no): ")
                    if save_choice.lower() == 'yes':
                        # Використання DataHandler для збереження даних
                        DataHandler.save_data(table.get_string(), 'txt')
                        print("Data saved to books.txt")
                else:
                    print("No books available.")

            elif choice == '2':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                if self.validate_input(r'^[A-Za-z0-9\s]+$', title) and self.validate_input(r'^[A-Za-z\s]+$', author):
                    response = self.library.add_book(title, author)
                    if response:
                        print(f"Book added: {response}")
                    else:
                        print("Failed to add book.")
                else:
                    print("Invalid input. Please enter valid title and author.")

            elif choice == '3':
                title = input("Enter book title to search: ")
                books = self.library.search_books(title)
                print("Books found:", books)

            elif choice == '4':
                print("Thank you for using the Library API Service!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    @staticmethod
    def validate_input(regex, input_text):
        if not re.match(regex, input_text):
            logging.error("Invalid input")
            return False
        return True

def main():
    client = APIClient()
    library = Library(client)
    ui = UI(library)
    ui.run()

if __name__ == '__main__':
    main()