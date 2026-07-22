# multiple_exceptions.py

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    operator = input("Enter operator (+ - * /): ")

    if operator == "+":
        print("Answer:", first + second)

    elif operator == "-":
        print("Answer:", first - second)

    elif operator == "*":
        print("Answer:", first * second)

    elif operator == "/":
        print("Answer:", first / second)

    else:
        raise ArithmeticError("Invalid operator.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

except ArithmeticError as error:
    print(error)