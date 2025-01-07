# Decorators:(Property)
class Student():
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage = str((self.chem + self.phy + self.math) / 3) + "%"
        # percentage
        '''
    def calcPercentage(self):
        self.percentage = str((self.chem + self.phy + self.math) / 3) + "%"
        '''
    @property
    def percentage(self):
        return str((self.chem + self.phy + self.math) / 3) + "%"
'''
@property Decorator or any method in the class to use the method as a property.
There are two more decorators available: getter & setter.
'''
stu1 = Student(92,95,77)
print(stu1.percentage)

stu1.math = 87
print(stu1.phy)
# stu1.calcPercentage()
print(stu1.percentage) # % is not changing acc to new value