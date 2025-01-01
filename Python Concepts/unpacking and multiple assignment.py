# Unpacking and Multiple Assignment

# Multiple Assignment
a,b,c = 1,2,3
print(a,b,c) # 1 2 3
'''
Unpacking
'''
my_tuple = (10, 20, 30)
# x, y, z = my_tuple == *x,z = my_tuple
*x,z = my_tuple
print(my_tuple) # (10, 20, 30)
'''
Swapping Values
'''
a,b =b,a
print(a,b) # 2 1
'''
temp =a
a = b
b = temp
'''




