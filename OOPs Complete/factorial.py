def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(0, 10):
    print(factorial(i),end="|")