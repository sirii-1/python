# classes_objects.py

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Details")
        print("----------------")
        print("Name     :", self.name)
        print("Roll No  :", self.roll_no)
        print("Marks    :", self.marks)

    def grade(self):
        if self.marks >= 90:
            print("Grade    : A")
        elif self.marks >= 75:
            print("Grade    : B")
        elif self.marks >= 60:
            print("Grade    : C")
        else:
            print("Grade    : D")


student1 = Student("Siri", 60 , 88)

student1.display()
student1.grade()