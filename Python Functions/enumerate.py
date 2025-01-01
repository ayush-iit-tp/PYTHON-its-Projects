# ENUMERATE

tasks = ["Write report","Attend meeting","Review Code","Submit timesheet"]

for i in range(len(tasks)):
    task =tasks[i]
    print(f"{i + 1}. {task}")
'''
1. Write report
2. Attend meeting
3. Review Code
4. Submit timesheet
'''

'''
Enumerate: This function adds a counter to an iterable 
and returns it as an enumerate object. 
You can specify the starting value of 
the counter with the start parameter.
'''
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")

'''
1. Write report
2. Attend meeting
3. Review Code
4. Submit timesheet
'''



