# Static Methods don't have any self inside them.
# They work at Class level & not on Object level.
# Decorator
class Marvel:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    @staticmethod  # Decorator
    def CU():
        print("MCU")

s1 = Marvel("Iron Man","Technology")
print(s1.name, "has the ability:", s1.ability, "and he belongs to:", end=" ")
s1.CU()  # Call the static method correctly










