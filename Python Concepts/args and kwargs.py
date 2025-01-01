# *args & ** kwargs

def print_all(*args, **kwargs):
    print("Positional Arguments", args)
    print("Keyword Arguments", kwargs)
'''
*args & ** kwargs
allows you to accept unlimited
number of positional and keyword arguments
'''
print_all(1,2,3, name="Alice", age=30)
'''
Output:
Positional Arguments (1, 2, 3)
Keyword Arguments {'name': 'Alice', 'age': 30}
'''










