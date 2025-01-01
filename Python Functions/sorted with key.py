people = [
    {"name":"ALICE","age":30},
    {"name":"HELEN","age":34},
    {"name":"ESTELLA","age":26},
    {"name":"PIP","age":27},
]
#sorted_num = sorted(numbers) see the difference
sorted_people = sorted(people, key=lambda person: person["age"])
#sort according to their age
print(sorted_people)
'''
[{'name': 'ESTELLA', 'age': 26}, 
{'name': 'PIP', 'age': 27}, 
{'name': 'ALICE', 'age': 30}, 
{'name': 'HELEN', 'age': 34}]
'''





