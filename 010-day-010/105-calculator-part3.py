import art

num1 = ""
num2 = ""
num3 = ""
operation_symbol = ""
operations = ""
answer = ""
repeat = "y"


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    """Ask for number and operation"""
    global num1, num2, operation_symbol, answer
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while len(operation_symbol) != 1:
        operation_symbol = input(f"Pick an operation from the line above.\n{num1} ")
    num2 = int(input(f"What's the second number?\n{num1} {operation_symbol} "))
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

def repeat_calculator():
    global repeat, answer, operation_symbol
    repeat = input(f'Type "y" to continue calculating with {answer}, or type "n" to exit.: ')
    num1 = answer
    operation_symbol = input(f"Pick an operation symbol.\n{answer} ")
    num2 = int(input(f"Whats the new number?\n{answer} {operation_symbol} "))
    answer = (calculation_function(num1, num2))
    print(f"{num1} {operation_symbol} {num2} = {answer}")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
calculator()
calculation_function = operations[operation_symbol]
while repeat == "y":
    repeat_calculator()

