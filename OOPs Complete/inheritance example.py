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

car1 = HondaCar("Amaze")
car2 = HondaCar("Elevate")

print(car1.name,end=" | ")
print(car1.color,end=" color | ")
car1.start()

print(car2.name)