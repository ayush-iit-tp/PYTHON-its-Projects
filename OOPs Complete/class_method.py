class Superhero:
    def __init__(self, name, power):
        name = 'Anonymous'

        @classmethod
        def changeName(cls, name):
            cls.name = name
'''
class Person:
    name = 'Anonymous'

    def changeName(self, name):
        #self.name = name
        self.__class__.name = name
        Person.name = name
'''
p1 = Person()
p1.changeName("Ayush Yadav")
print(p1.name)     # Ayush Yadav
print(Person.name) # Ayush Yadav
