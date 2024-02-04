# This is a calculator

def summ(a,b):
    try:
        result = a + b
        return a + b
    except:
        return False

def sub(a,b):
    try:
        result = a - b
        return a - b
    except:
        return False

def mul(a,b):
    try:
        result = a * b
        return a * b
    except:
        return False

def div(a,b):
    try:
        result = a / b
        return a / b
    except:
        return False

possible_operations = ["sum", "sub", "mul", "div"]
possible_bool = ["True", "False"]

while True:
    operation = input("Enter the operation([sum] for sum, [sub] for subtraction, [mul] for multiplication and [div] for division): ")
    if operation not in possible_operations:
        print("Incorrect input, try again.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("You did not type a number, repeat the process and try again.")
        continue

    if operation == possible_operations[0]:
        result = summ(a,b)
        character = "+"
    elif operation == possible_operations[1]:
        result = sub(a,b)
        character = "-"
    elif operation == possible_operations[2]:
        result = mul(a,b)
        character = "x"
    else:
        result = div(a,b)
        character = ":"

    if result is False:
        print("ERROR........")
        continue

    print(a, character, b, "=", result)

    while True:
        try_again = input("Want to make another operation? Type [True] if yes or [False] if not: ")
        if try_again in possible_bool:
            break
        else:
            print("Invalid input. Type [True] or [False].")

    if try_again == "False":
        print("End. Thanks for using the calculator!")
        break
