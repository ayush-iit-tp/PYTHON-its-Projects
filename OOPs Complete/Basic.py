# When a function calls itself

# With Recursion
def show(n):
    if n == -1:
        return
    print(n,end = "|")
    show(n-1) # using Recursion

show(15)

'''
Print n to 0 backwards

# Without recursion
def show(n):
    print(n)

#Base Case
if n == 0:
    return  # to break the loop
'''








