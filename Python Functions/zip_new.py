# ZIP Function
# names = ["Alice", "Bob", "Charlie", "David", "Estella"]
# ages = [30, 25, 35, 20, 26]
# genders = ["F", "M", "M", "M", "F"]
#
# combined = list(zip(names, ages, genders))
# print(combined)
'''
[('Alice', 30, 'F'), ('Bob', 25, 'M'), ('Charlie', 35, 'M'), ('David', 20, 'M'), ('Estella', 26, 'F')]
'''
# for name,age,gender in combined:
#     print(f"{name} is {age} years old and is {gender}.")
'''
Alice is 30 years old and is F.
Bob is 25 years old and is M.
Charlie is 35 years old and is M.
David is 20 years old and is M.
Estella is 26 years old and is F.
'''

'''
    What if ?
'''
names = ["Alice", "Bob", "Charlie", "David", "Estella"]
ages = [30, 25, 35, 20, 26]
genders = ["F", "M"]

combined = list(zip(names, ages, genders))
print(combined)
'''
[('Alice', 30, 'F'), ('Bob', 25, 'M'), ('Charlie', 35, 'M'), ('David', 20, 'M'), ('Estella', 26, 'F')]
'''
for name, age, gender in combined:
    print(f"{name} is {age} years old and is {gender}.")
    '''
Alice is 30 years old and is F.
Bob is 25 years old and is M.
    '''
    '''
Only two lines will be printed, Because 
genders = ["F", "M"]  HAS MIN 2 ITEMS ONLY
    '''











