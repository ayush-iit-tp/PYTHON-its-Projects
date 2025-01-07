class Circle:
    def __init__(self, radius):
        self.radius = float(radius)
    def area(self):
        return (22/7) * self.radius ** 2
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

c2 = Circle(14)
print(c2.area())
print(c2.perimeter())