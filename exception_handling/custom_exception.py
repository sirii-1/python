# custom_exception.py

class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100.")

    print("Marks Accepted")

except InvalidMarksError as error:
    print(error)

except ValueError:
    print("Please enter numeric marks only.")