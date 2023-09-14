import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    """Asks for input, calculates inputs, repeats"""
    repeat_calculator = True

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while repeat_calculator:
        operation_symbol = input(f"Pick an operation.\n{num1} ")
        calculation_function = operations[operation_symbol]
        num2 = float(input(f"What's the second number?\n{num1} {operation_symbol} "))

        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f'Type "y" to continue calculating with {answer}, press any key to restart. "control + c" to quit: ') != "y":
            repeat_calculator = False
            calculator()
        num1 = answer

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)
calculator()

