class Car:
    color = "black"
    @staticmethod
    def start():
        print("Starting")

    @staticmethod
    def stop():
        print("Stopping")

class HondaCar(Car):
    def __init__(self, name):
        self.name = name

class Aamaze(HondaCar):
    def __init__(self, type):
        self.type = type

car1 = Aamaze("Petrol")
car1.start()