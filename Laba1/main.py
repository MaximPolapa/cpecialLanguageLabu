import math
import logging

class Memory:
    def __init__(self):
        self.memory = []

    def store(self, expression, result):
        self.memory.append((expression, result))

    def recall(self):
        return self.memory

    def clear(self):
        self.memory = []

class Calculator:
    def __init__(self):
        self.memory = Memory()

    def calculate(self, num1, num2, operator):
        operator_functions = {
            '+': lambda: num1 + num2,
            '-': lambda: num1 - num2,
            '*': lambda: num1 * num2,
            '/': lambda: num1 / num2 if num2 != 0 else "Error: division on zero",
            '^': lambda: num1 ** num2,
            '√': lambda: math.sqrt(num1) if num1 >= 0 else "Error: negative number under the root",
            '%': lambda: num1 % num2 if num2 != 0 else "Error: division on zero"
        }
        operation = operator_functions.get(operator)
        if operation is None:
            return "Error: missing operator, try again"
        try:
            return operation()
        except ZeroDivisionError:
            return "Error: division by zero"
        except ValueError:
            return "Error: invalid input"

    def run(self):
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

            memory_values = self.memory.recall()
            print("Memory operator:")
            for expression, result in memory_values:
                print(f"{expression} = {result}")

            repeat = input("Do you want to continue? (yes/no): ")
            if repeat.lower() != 'yes':
                break

def main():
    calc = Calculator()
    calc.run()

if __name__ == "__main__":
    main()
