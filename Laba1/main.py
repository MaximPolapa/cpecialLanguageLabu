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
            return "Error: division on zero"
    elif operator == '^':
        return num1 ** num2
    elif operator == '√':
        if num1 >= 0:
            return math.sqrt(num1)
        else:
            return "Error: negative number under the root"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: division on zero"
    else:
        return "Error: messing operator, try again"

memory = Memory()

while True:
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Secons number: "))
    except ValueError:
        print("Error: it`s wrote not number, try again")
        continue

    while True:
        operator = input("Choose operator (+, -, *, /, ^, √, %): ")
        if operator in ['+', '-', '*', '/', '^', '√', '%']:
            result = calculate(num1, num2, operator)
            print(f"Result: {result}")
            memory.store(f"{num1} {operator} {num2}", result)
            break
        else:
            print("Error: bad operator. Please, choose on of this operator '+, -, *, /, ^, √, %' ")

    memory_values = memory.recall()
    print(f"Memory operator:")
    for expression, result in memory_values:
        print(f"{expression} = {result}")
    repeat = input("Do you want continued? (yes/no): ")
    if repeat.lower() != 'yes':
        break
