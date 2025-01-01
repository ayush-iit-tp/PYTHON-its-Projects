# List Comprehensions
squares = [x**2
           for x in range(10)]
print(squares)
'''
x**2 for x in range(10)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
evens = [x
         for x in range(10)
         if x % 2 ==0]
print(evens)
'''
x for x in range(10) if x % 2 ==0
[0, 2, 4, 6, 8]
'''
nested = [[1,2],[3,4],[5,6]]
flattened = [item
             for sublist in nested
             for item in sublist]
print(flattened)
'''
item for sublist in nested for item in sublist
[1, 2, 3, 4, 5, 6]
'''
cartesian_product = [(x,y)
                     for x in range(2)
                     for y in 'abc']
print(cartesian_product)
'''
(x,y) for x in range(2) for y in 'abc'
[(0, 'a'), (0, 'b'), (0, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]
'''










