"""Required modules"""
import os
import unittest
from logging.config import dictConfig

from share.console_io.console_output import ConsoleOutput
from share.console_io.console_input import ConsoleInput
from share.config import Config
from share.menu import Menu, menu_item

from subsystems.lab1.main import main as lab1
from subsystems.lab2.main import main as lab2

from subsystems.lab3.src.ascii_art_maker import AsciiArtMaker

from subsystems.lab4.src.core.app import App
from subsystems.lab4.src.core.console_inputter import ConsoleInputter
from subsystems.lab4.src.core.graphic import Graphic

from subsystems.lab5.main import main as lab5
from subsystems.lab6.main import main as lab6
from subsystems.lab7.main import main as lab7
from subsystems.lab8.main import main as lab8


class Runner(Menu):
    """Facade for running Python scripts through a console menu"""

    def __init__(self):
        super().__init__("Python Runner", "Select a subsystem to run")

    def run(self):
        """Start to show the menu to allow script selection"""
        self.show()

    @menu_item(title="Calulator")
    def lab1(self) -> None:
        """Lab 1 Standard Python Calculator"""
        lab1()

    @menu_item(title="OOP Calulator")
    def lab2(self) -> None:
        """Lab2 OOP Calculator"""
        lab2()

    @menu_item("ASCII Arts")
    def lab3(self) -> None:
        """Lab3 ACSII Arts"""
        art_maker = AsciiArtMaker()
        art_maker.run()

    @menu_item("ASCII Art without libs")
    def lab4(self) -> None:
        """Lab4 ASCII Art no libraries"""
        inputter = ConsoleInputter()
        size = os.get_terminal_size() 
        outputter = Graphic(size.columns, size.lines)

        app = App(inputter, outputter)
        app.run()

    @menu_item("ASCII Art 3D")
    def lab5(self) -> None:
        """Lab5 ASCII Art 3D"""
        lab5()

    @menu_item("Unit tests")
    def lab6(self) -> None:
        """Lab6 Unit tests with oop calulator"""
        lab6()

    @menu_item("API")
    def lab7(self) -> None:
        """Lab7 Api"""
        lab7()
        
    
    @menu_item("CSV visualizer")
    def lab8(self) -> None:
        """Lab8 CSV visualizer"""
        lab8()

def main() -> None:
    """ Main function to run as script from shell """
    config = Config("config.json")
    dictConfig(config["logging"])
    
    runner = Runner()
    runner.run()

if '__main__' == __name__:
    main()

    # menu = ConsoleMenu("Runner")
    # menu.append_item(FunctionItem("Calculator", lab1.main.main))
    # menu.append_item(FunctionItem("OOP Calculator", lab2.main.main))
    # menu.append_item(FunctionItem("ASCII Art", lab3.main.main))
    # menu.append_item(FunctionItem("2D ASCII Art without additional libraries", lab4.main.main))
    # menu.append_item(FunctionItem("3D ASCII Arts", lab5.main.main))
    # menu.append_item(FunctionItem("Unit tests", lab6.main.main))
    # menu.append_item(FunctionItem("API requests", lab7.main.main))
    # menu.append_item(FunctionItem("Visualize csv files", lab8.main.main))

    # menu.show()
