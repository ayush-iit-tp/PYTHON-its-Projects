class Person:
    __name = "Ayush"
    def __hello(self):
        print("Hello!")

    def welcome(self):
        self.__hello()
        #print("Welcome " + self.__name)
p1 = Person()

print(p1.welcome())