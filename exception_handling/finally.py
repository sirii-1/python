# finally.py

file = None

try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist.")

finally:
    if file:
        file.close()
        print("File closed successfully.")

    print("Program finished.")