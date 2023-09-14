import art

num1 = ""
num2 = ""
operation_symbol = ""
operations = ""
answer = ""


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def user_inputs():
    """Ask for number and operation"""
    # global num1, num2, operation_symbol
    # num1 = int(input("What's the first number?: "))
    # for symbol in operations:
    #     print(symbol)
    # operation_symbol = input("Pick an operation from the line above: ")
    # num2 = int(input("What's the second number?: "))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#user_inputs()
num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the third number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")