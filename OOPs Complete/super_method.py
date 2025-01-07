class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Starting")

    @staticmethod
    def stop():
        print("Stopping")

class HondaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        '''
        If you want to call any method of parent class then call through super.
        '''
        self.name = name
        super().start()

car1 = HondaCar("Amaze","Petrol")
print(car1.type)











