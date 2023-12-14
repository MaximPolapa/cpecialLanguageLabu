import math
import logging

class Memory:
    """
    A class to store and manage the memory of calculations.
    """
    def __init__(self):
        # Initialize an empty list to store calculation results
        self.memory = []

    def store(self, expression, result):
        """
        Store a calculation and its result in memory.

        Parameters:
        expression (str): The calculation expression.
        result (float): The result of the calculation.
        """
        self.memory.append((expression, result))

    def recall(self):
        """
        Retrieve all stored calculations and their results.

        Returns:
        list: A list of tuples containing expressions and their results.
        """
        return self.memory

    def clear(self):
        """
        Clear all stored calculations from memory.
        """
        self.memory = []

class Calculator:
    """
    A simple calculator class capable of basic arithmetic operations.
    """
    def __init__(self):
        # Initialize the Memory class to handle calculation history
        self.memory = Memory()

    def calculate(self, num1, num2, operator):
        """
        Perform a calculation based on the given operator.

        Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The operator for the calculation.

        Returns:
        float or str: The result of the calculation or an error message.
        """
        # Dictionary mapping operators to their corresponding lambda functions
        operator_functions = {
            '+': lambda: num1 + num2,
            '-': lambda: num1 - num2,
            '*': lambda: num1 * num2,
            '/': lambda: num1 / num2 if num2 != 0 else "Error: division on zero",
            '^': lambda: num1 ** num2,
            '√': lambda: math.sqrt(num1) if num1 >= 0 else "Error: negative number under the root",
            '%': lambda: num1 % num2 if num2 != 0 else "Error: division on zero"
        }

        # Retrieve the appropriate function based on the operator
        operation = operator_functions.get(operator)
        if operation is None:
            return "Error: missing operator, try again"

        # Execute the operation and handle potential errors
        try:
            return operation()
        except ZeroDivisionError:
            return "Error: division by zero"
        except ValueError:
            return "Error: invalid input"

    def run(self):
        """
        Run the calculator interface in a loop until the user decides to exit.
        """
        while True:
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
            except ValueError:
                logging.info("Error in type of number")
                print("Error: it's not a number, try again")
                continue

            operator = input("Choose operator (+, -, *, /, ^, √, %): ")
            if operator in ['+', '-', '*', '/', '^', '√', '%']:
                result = self.calculate(num1, num2, operator)
                print(f"Result: {result}")
                self.memory.store(f"{num1} {operator} {num2}", result)
            else:
                print("Error: bad operator. Please, choose one of '+, -, *, /, ^, √, %'")
                logging.info("ERROR in type operator")

            # Display the memory after each calculation
            memory_values = self.memory.recall()
            print("Memory operator:")
            for expression, result in memory_values:
                print(f"{expression} = {result}")

            # Ask the user if they want to continue
            repeat = input("Do you want to continue? (yes/no): ")
            if repeat.lower() != 'yes':
                break

def main():
    """
    Main function to run the calculator application.
    """
    calc = Calculator()
    calc.run()

if __name__ == "__main__":
    main()
