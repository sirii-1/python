students = []

with open("students.txt", "r") as file:
    for line in file:
        roll, name, marks, grade = line.strip().split(",")
        students.append({
            "roll": roll,
            "name": name,
            "marks": int(marks),
            "grade": grade
        })

students.sort(key=lambda x: x["marks"], reverse=True)

print("\n----- Student Report -----")

total = 0
grades = {}

for i, student in enumerate(students, start=1):
    print(f"{i}. {student['name']} ({student['roll']})")
    print(f"   Marks : {student['marks']}")
    print(f"   Grade : {student['grade']}")

    total += student["marks"]

    grades[student["grade"]] = grades.get(student["grade"],0)+1

average = total/len(students)

print("\nTopper :", students[0]["name"])
print("Lowest :", students[-1]["name"])
print("Average :", round(average,2))

print("\nGrade Distribution")

for g,c in grades.items():
    print(g,"=",c)