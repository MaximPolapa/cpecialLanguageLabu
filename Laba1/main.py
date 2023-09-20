import math
#Class memory to save inf about users 
class Memory:
    def __init__(self): #init func to memory storage
        self.memory = []
    def store(self, expression, result): #add func to memory storage
        self.memory.append((expression, result))
    def recall(self): #return inf from starage
        return self.memory
    def clear(self): #clear func to storage
        self.memory = []

def calculate(num1, num2, operator): 
    operator_functions = {
        '+': lambda: num1 + num2,
        '-': lambda: num1 - num2,
        '*': lambda: num1 * num2,
        '/': lambda: num1 / num2 if num2 != 0 else "Error: division on zero",
        '^': lambda: num1 ** num2,
        '√': lambda: math.sqrt(num1) if num1 >= 0 else "Error: negative number under the root",
        '%': lambda: num1 % num2 if num2 != 0 else "Error: division on zero"
    }
    operation = operator_functions.get(operator) #get operator
    if operation is None:
        return "Error: missing operator, try again"
    try:
        return operation()
    except ZeroDivisionError:
        return "Error: division by zero"
    except ValueError:
        return "Error: invalid input"

memory = Memory()

while True:
    try:
        num1 = float(input("First number: ")) #first number
        num2 = float(input("Secons number: ")) #second number
    except ValueError:
        print("Error: it`s wrote not number, try again")
        continue
    while True:
        operator = input("Choose operator (+, -, *, /, ^, √, %): ") #operator
        if operator in ['+', '-', '*', '/', '^', '√', '%']: #find which operator was change
            result = calculate(num1, num2, operator)
            print(f"Result: {result}")
            memory.store(f"{num1} {operator} {num2}", result)
            break
        else:
            print("Error: bad operator. Please, choose on of this operator '+, -, *, /, ^, √, %' ")

    memory_values = memory.recall() #return inf from storage memory
    print(f"Memory operator:")
    for expression, result in memory_values:
        print(f"{expression} = {result}")
    repeat = input("Do you want continued? (yes/no): ")
    if repeat.lower() != 'yes':
        break
