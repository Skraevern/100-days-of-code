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
    global num1, num2, operation_symbol
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

user_inputs()

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")