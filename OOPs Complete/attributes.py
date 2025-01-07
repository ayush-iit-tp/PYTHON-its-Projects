def nat():
    return 0
'''
# Attributes
 Two types:
# Class attribute which is common to all objects
    example college name of all students
# Another is object attribute which is unique to every object
    name & roll-no of all students
# Always object attr > class attr

# Then What are methods ?
All functions inside Class are methods
'''

class Student:
    college_name = 'IIT_Tirupati'

    def __init__(self, name, roll_no): # self will be first & always should be there
        self.name = name
        self.roll_no = roll_no

    def hello(self):
        print('Hello Student:', self.name)

s1 = Student('Ayush', 114)
s1.hello()
print(s1.college_name)
print(s1.roll_no)







