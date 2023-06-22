from art import logo

print(logo)


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    is_repeat = True
    while is_repeat:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_req = input(
            f"Type 'y' to continue calculatng with {answer} , or type 'n' to start a new calculations.: ")
        if continue_req == 'y':
            num1 = answer
        else:
            is_repeat = False
            calculator()


calculator()