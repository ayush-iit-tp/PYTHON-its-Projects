def mutation(Lst):
    Lst.append(10)
    return Lst
'''
Immutable means once define them, they can't be changed later on.
All int float boolean string are immutable
List set Dictionary & Python Objects all are Mutable means they can be changed later on
'''

my_numbers = [1, 2, 3]
list_after_call = (mutation(my_numbers))

print("My Numbers:", my_numbers)
print("List after call:", list_after_call)

# Here we are modifying our old list acc to us
# But we can't do this to a string
''' Please notice below what we are going to do:
'''

def mutation(Lst=[]):
    Lst.append(10)
    return Lst

mutation()
mutation()
mutation()

print(mutation())

''' Solution is : [10, 10, 10, 10] 
How?
till we are calling print(mutation()) 
three 10 are already being stored in the list Lst
4TH TIME WHEN WE ARE PRINTING then all 4 10 are being printed
'''
