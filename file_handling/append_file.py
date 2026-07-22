existing_rolls = set()

try:
    with open("students.txt", "r") as file:
        for line in file:
            roll = line.split(",")[0]
            existing_rolls.add(roll)
except FileNotFoundError:
    pass


def grade(m):
    if m>=90:
        return "A+"
    elif m>=80:
        return "A"
    elif m>=70:
        return "B"
    elif m>=60:
        return "C"
    elif m>=50:
        return "D"
    return "F"


n = int(input("Students to Add: "))

with open("students.txt","a") as file:

    for i in range(n):

        roll=input("Roll: ")

        if roll in existing_rolls:
            print("Duplicate Roll Number!")
            continue

        name=input("Name: ")
        marks=int(input("Marks: "))

        file.write(f"{roll},{name},{marks},{grade(marks)}\n")

        existing_rolls.add(roll)

print("Database Updated Successfully")