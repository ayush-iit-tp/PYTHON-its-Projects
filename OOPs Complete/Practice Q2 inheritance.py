class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("Role:", self.role)
        print("Dept:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","VLSI", "75000")

# e1 = Employee("DFT Engineer", "Validation", 200000)
# e1.showDetails()

e1 = Engineer("Ayush","26")
e1.showDetails()












