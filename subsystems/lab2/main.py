import math
import gettext
import locale
import logging

# Memory class for storing user inputs and results
class Memory:
    def __init__(self):
        self.memory = []

    def store(self, expression, result):
        self.memory.append((expression, result))

    def recall(self):
        return self.memory

    def clear(self):
        self.memory = []

# Calculator class for performing calculations
class Calculator:
    def __init__(self, locale, gettext_func):
        self.memory = Memory()
        self.locale = locale
        self._ = gettext_func  # Зберігаємо функцію локалізації як атрибут класу
        self.OPERATORS = {
            '+': lambda num1, num2: num1 + num2,
            '-': lambda num1, num2: num1 - num2,
            '*': lambda num1, num2: num1 * num2,
            '/': lambda num1, num2: num1 / num2 if num2 != 0 else self._("Error: division on zero"),
            '^': lambda num1, num2: num1 ** num2,
            '√': lambda num1, _: math.sqrt(num1) if num1 >= 0 else self._("Error: negative number under the root"),
            '%': lambda num1, num2: num1 % num2 if num2 != 0 else self._("Error: division on zero")
        }

    def get_input(self, prompt_key):
        return float(input(questions[self.locale][prompt_key]))

    def run(self):
        while True:
            num1 = self.get_input('first_number')
            num2 = self.get_input('second_number')

            operator = input(questions[self.locale]['operator'])
            if operator in self.OPERATORS:
                result = self.OPERATORS[operator](num1, num2)
                print(self._("Result:"), result)
                expression = f"{num1} {operator} {num2}"
                self.memory.store(expression, result)
            else:
                print(self._("Error: Invalid operator. Please choose one of these operators: '+, -, *, /, ^, √, %' "))
                logging.info("ERROR in type of operator")

            memory_values = self.memory.recall()
            print(self._("Memory operator:"))
            for expression, result in memory_values:
                print(f"{expression} = {result}")

            repeat = input(questions[self.locale]['continue']).strip().lower()
            if repeat != 'так' and repeat != 'yes':
                break

# Set the default language to Ukrainian
locale.setlocale(locale.LC_ALL, 'uk_UA.utf8')

# Function to choose the language
def choose_language():
    language = input("Оберіть мову | Choose language (укр/eng): ").strip().lower()
    if language == "eng":
        return 'en_US'
    elif language == "укр":
        return 'uk_UA'
    else:
        print("Непідтримувана мова, обрана українська.")
        logging.info("ERROR in type of language")
        return 'uk_UA'

# Dictionary for localized prompts and messages
questions = {
    'en_US': {
        'first_number': "First number: ",
        'second_number': "Second number: ",
        'operator': "Choose operator (+, -, *, /, ^, √, %): ",
        'continue': "Do you want to continue? (yes/no): "
    },
    'uk_UA': {
        'first_number': "Перше число: ",
        'second_number': "Друге число: ",
        'operator': "Оберіть операцію (+, -, *, /, ^, √, %): ",
        'continue': "Бажаєте продовжити? (так/ні): "
    }
}

def main():
    selected_locale = choose_language()
    gettext_func = gettext.translation('calculator', localedir='locales', languages=[selected_locale], fallback=True).gettext
    calculator = Calculator(selected_locale, gettext_func)
    calculator.run()

if __name__ == "__main__":
    main()
