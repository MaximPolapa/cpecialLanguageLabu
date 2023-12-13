import logging
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

# Importing the lab modules
from Laba1.main import main as lab1
from Laba2.main import main as lab2
from Laba3.main import main as lab3
from Laba4.main import main as lab4
from Laba5.main import main as lab5
from Laba6.main import main as lab6
from Laba7.main import main as lab7
from Laba8.main import main as lab8


logging.basicConfig(filename="logs/app.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MenuFacade:
    def __init__(self):
        self.menu = ConsoleMenu("Runner")
        logging.info("MenuFacade instance created")

    def add_item(self, title, action):
        self.menu.append_item(FunctionItem(title, action))
        logging.info(f"Menu item '{title}' added")

    def show_menu(self):
        logging.info("Displaying menu")
        self.menu.show()

def main():
    logging.info("Application started")
    menu_facade = MenuFacade()

    menu_facade.add_item("Calculator", lab1)
    menu_facade.add_item("OOP Calculator", lab2)
    menu_facade.add_item("ASCII Art", lab3)
    menu_facade.add_item("2D ASCII Art without additional libraries", lab4)
    menu_facade.add_item("3D ASCII Arts", lab5)
    menu_facade.add_item("Unit tests", lab6)
    menu_facade.add_item("API requests", lab7)
    menu_facade.add_item("CSV File", lab8)

    menu_facade.show_menu()
    logging.info("Application finished")

if __name__ == '__main__':
    main()
