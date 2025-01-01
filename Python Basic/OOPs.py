# class is an template from which objects can be made.
# example: You wan to fill railway reservation form
# class is an empty form
# OBJECT will be an filled form

# class employee:
#
#     salary = 98000
#     name = "Ayush"
#
# ayush = employee()
# print(ayush.salary)
# print(ayush.name)

# It will print this:
# 98000
# Ayush

# class employee:
#
#     salary = 98000
#     name = "Ayush"
#
# # You can define methods
#     # within a class to access or
#     # modify the properties of an object like this below:
#     def getSalary(self):
#         return self.salary
#
# ayush = employee()
# print("Getting Salary using Object",ayush.salary)
# print("Getting Salary using Function",ayush.getSalary())
# print(ayush.name)

# USE OF CONSTRUCTOR

class Employee:
    def __init__(self, name, age, salary): # define constructor like this
        self.name = name
        self.age = age
        self.salary = salary

    def getsalary(self):
            print(self.salary)

# MAKING NEW OBJECT NAME AYUSH
ayush = Employee("Ayush","26 years old","SALARY is 98000")
print(ayush.name)
print(ayush.age)
#print(ayush.salary)
ayush.getsalary()

# MAKING NEW OBJECT NAME ALI
ali = Employee("Ali","25 years old","SALARY is 96000")
print(ali.name)
print(ali.age)
# print(ali.salary)
ali.getsalary()














































































