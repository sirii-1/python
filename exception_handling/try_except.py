# try_except.py

try:
    username = input("Enter username: ")

    password = int(input("Enter 4-digit PIN: "))

    if password != 1234:
        raise PermissionError("Invalid PIN")

    print(f"Welcome, {username}!")

except ValueError:
    print("PIN must contain only numbers.")

except PermissionError as error:
    print(error)