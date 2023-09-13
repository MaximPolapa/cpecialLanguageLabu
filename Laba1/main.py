import math

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

while True:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: ")) 
    while True:
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if operator in ['+', '-', '*', '/', '^', '√', '%']:
            result = calculate(num1, num2, operator)
            print(f"Результат: {result}")
            break
        else:
            print("Помилка: недійсний оператор. Будь ласка, введіть один із +, -, *, /, ^, √, %.")

   
    repeat = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
    if repeat.lower() != 'так':
        break
