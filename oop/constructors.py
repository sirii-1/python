# constructors.py

class Employee:

    company = "Google"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("Employee Information")
        print("--------------------")
        print("Company    :", Employee.company)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Salary     :", self.salary)


emp1 = Employee("Rahul", "Marketing", 65000)
emp2 = Employee("Anjali", "HR", 58000)

emp1.display()
print()
emp2.display()