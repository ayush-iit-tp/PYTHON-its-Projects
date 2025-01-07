from OOPs import attributes


class Superhero:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
s1 = Superhero("Superman", "Super")
print(s1.name)
print(s1.ability)

class Account:
    def __init__(self, name, balance, acc_no):
        self.name = name
        self.balance = balance
        self.__acc_no = acc_no
        '''
# Use two _ before any attribute to make it private
This private attribute is within the class       
        '''
    def reset_password(self):
            print("Reset password of account",self.__acc_no)
# End of class
acc1 = Account("Bob", 10000, "12345")
'''
# These print statements are outside class
'''
print(acc1.name)
print(acc1.balance)
print(acc1.reset_password()) # private attribute
print(acc1.__acc_no) # public attribute


