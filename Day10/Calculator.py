

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def square_root(a, b):
    return pow(a, b)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "sr": square_root
}


def calculator():
    first_number = float(input("What's the first number?:"))
    game_off = False
    while not game_off:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation:")
        if operation_symbol != "sr":
            second_number = float(input("What's the next number?:"))
        else:
            second_number = 0.5

        answer = operations[operation_symbol]
        result = answer(first_number, second_number)

        if operation_symbol != "sr":
            print(f'{first_number} {operation_symbol} {second_number} = {result}')
        else:
            print(f'Square root of {first_number} = {result}')

        next_game = input(
            f"Type 'y' to continue calculating with {result}, type 'n' to start new calculation, 'exit' to end program:")
        if next_game == 'y':
            first_number = result
        elif next_game == 'n':
            game_off = True
            calculator()
        elif next_game == 'exit':
            game_off = True
        else:
            print('invalid input, run program again')


calculator()
