def mutation(Lst=None):
    if Lst == None:
        Lst = []
    Lst.append(10)
    return Lst

mutation()
mutation()
mutation()

print(mutation())
''' Sol is [10] only
How ?
Because if the list in none then create a new list everytime
In your function mutation, the default value for Lst is None, and if Lst is None, a new list is created. 
However, each time you call mutation(), a new list is created because Lst is set to None by default.
'''



