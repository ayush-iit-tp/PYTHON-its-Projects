# Slicing works on Lists Strings Tuples

my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4]) #[ 1, 2, 3]
print(my_list[:2]) # [0, 1] First 2 elements
print(my_list[::2]) # [0, 2, 4] Every 2nd element
'''
Reversed List
'''
print(my_list[::-1]) # [5, 4, 3, 2, 1, 0]
print(my_list[:-3:2]) # [0, 2]go to 3rd last element but don't include it
'''
A list will always be equal to: [start:end:step]
'''









