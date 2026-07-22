def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    return "F"


def write_students():
    try:
        n = int(input("Enter number of students: "))

        with open("students.txt", "w") as file:
            for i in range(n):
                print(f"\nStudent {i+1}")

                roll = input("Roll No: ")
                name = input("Name: ")

                while True:
                    marks = int(input("Marks (0-100): "))
                    if 0 <= marks <= 100:
                        break
                    print("Invalid Marks!")

                grade = calculate_grade(marks)

                file.write(f"{roll},{name},{marks},{grade}\n")

        print("\nDatabase Created Successfully!")

    except ValueError:
        print("Invalid Input")


write_students()