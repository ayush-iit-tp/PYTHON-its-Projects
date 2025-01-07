class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("Idli", 20)
ord2 = Order("Dosa", 30)
ord3 = Order("Tea", 10)
print(ord1 > ord2)
print(ord2 > ord3)
'''
use a dunder function: __gt__ means greater than func
'''











