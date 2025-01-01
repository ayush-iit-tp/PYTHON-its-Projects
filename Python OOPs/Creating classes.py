
class Dog(object):
    def __init__(self, name, age):   # self is mandatory for instances
        self.name = name
        self.age = age
    def speak(self):
        print("My name is" + self.name, 'and my age is' + self.age)

timothy = Dog('Timothy',45) # tim is an instance of type dog
timothy.speak()
prajual = Dog('Prajual',25)
prajual.speak()

'''
    Mandatory to write 
    def __init__(self):
    pass
'''










