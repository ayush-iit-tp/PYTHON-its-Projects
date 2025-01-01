# SORTED FUNC

numbers = [1, 2, 6, 8, 5, 3, 7, 4, 111, 10]
sorted_num = sorted(numbers)
print(sorted_num)
'''
[1, 2, 3, 4, 5, 6, 7, 8, 10, 111]
'''

sorted_num0 = sorted(numbers, reverse=True)
print(sorted_num0)
'''
[111, 10, 8, 7, 6, 5, 4, 3, 2, 1]
'''

# Sorting based on the length of the string representation of the numbers
sorted_num1 = sorted(numbers, key=lambda x: len(str(x)))
print(sorted_num1)
''' 
the numbers are sorted first by the 
length of their string representation, 
and then by their original order 
if the lengths are the same
[1, 2, 6, 8, 5, 3, 7, 4, 10, 111] 
'''




