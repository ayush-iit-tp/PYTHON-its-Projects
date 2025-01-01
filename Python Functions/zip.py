# ZIP Function
names = ["Alice", "Bob", "Charlie", "David"]
ages = [30, 25, 35, 20]

for i in range(min(len(names), len(ages))):
    name = names[i]
    age = ages[i]
    print(f"{name} is {age} years old")

'''
Alice is 30 years old
Bob is 25 years old
Charlie is 35 years old
David is 20 years old
'''

combined = list(zip(names, ages))
print(combined)
'''
[('Alice', 30), ('Bob', 25), ('Charlie', 35), ('David', 20)]
'''
for name,age in combined:
    print(f"{name} is {age} years old")

'''
Alice is 30 years old
Bob is 25 years old
Charlie is 35 years old
David is 20 years old
'''









