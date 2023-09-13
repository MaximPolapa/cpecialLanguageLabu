import math

class Memory:
    def __init__(self):
        self.memory = []

    def store(self, expression, result):
        self.memory.append((expression, result))

    def recall(self):
        return self.memory

    def clear(self):
        self.memory = []

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Помилка: ділення на нуль"
    elif operator == '^':
        return num1 ** num2
    elif operator == '√':
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Помилка: від'ємне число під коренем"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Помилка: ділення на нуль"
    else:
        return "Помилка: недійсний оператор"

memory = Memory()

while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: Ви вказали не число. Будь ласка, введіть число 1 або 2.")
        continue

    while True:
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if operator in ['+', '-', '*', '/', '^', '√', '%']:
            result = calculate(num1, num2, operator)
            print(f"Результат: {result}")

            memory.store(f"{num1} {operator} {num2}", result)
            break
        else:
            print("Помилка: недійсний оператор. Будь ласка, введіть один із +, -, *, /, ^, √, %.")

    memory_values = memory.recall()
    print(f"Значення в пам'яті:")
    for expression, result in memory_values:
        print(f"{expression} = {result}")

    repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
    if repeat.lower() != 'так':
        break
