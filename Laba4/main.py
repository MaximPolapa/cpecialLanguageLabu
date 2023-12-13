from .symbol import ascii_chars
from termcolor import colored
import os
import sys
from .ASCIIArt import ASCIIArt

class ASCIIArtApp:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            inp_text = input("Введіть текст: ")
            width = int(input("Введіть ширину об'єкту: "))
            height = int(input("Введіть висоту об'єкту: "))

            print("Доступні кольори:\n1. Білий\n2. Червоний")
            selected_color = input("Виберіть колір за номером: ")

            art = ASCIIArt(inp_text, width, height, selected_color)
            ascii_art = art.generate()
            print(ascii_art)

            preview_response = input("Бажаєте попередній перегляд збереженого ASCII-арт? (1 - Так, 0 - Ні): ")
            if preview_response == '1':
                art.save(ascii_art)

            restart_response = input("Бажаєте створити новий ASCII-арт? (1 - Так, 0 - Ні): ")
            if restart_response != '1':
                break

            os.system('cls' if os.name == 'nt' else 'clear')

def main():
    app = ASCIIArtApp()

if __name__ == "__main__":
    main()
