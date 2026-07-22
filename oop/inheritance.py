# inheritance.py

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display()
        print("Course :", self.course)


student = Student("Siri", 19 , "ECE")

student.display_student()