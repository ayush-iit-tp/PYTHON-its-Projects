# del Keyword: deletes object properties or entire object
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Baby_John", 25)
del s1.age
print(s1.name, s1.age)