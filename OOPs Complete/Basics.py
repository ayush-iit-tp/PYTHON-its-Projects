class Aliens:
# Default Constructor
    def __init__(self):
        pass

# User-defined/Parameterized Constructors
    def __init__(self, name, color):  # always should have an argument: self
        print("Adding new Alien.")
        self.name = name
        self.color = color

# All the data stored are called attributes

rath = Aliens("Rath", "Orange")
print(rath.name, "is", rath.color, "in color.")

alienx = Aliens("Alienx", "Black")
print(alienx.name, "is", alienx.color, "in color.")













