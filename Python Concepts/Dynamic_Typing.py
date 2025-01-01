# x = 10
# print(type(x))
#
# x ="Hello Python!"
# print(type(x))

def add(a: int, b: int) -> int:
    # IT IS DYNAMIC_TYPING
    if type(a) != int or type(b) != int:
        return "Invalid input"
    else:
        return a+b

print(add(10,20)) # Solution is coming
print(add("10",20)) # type error

# AFTER USING IF ELSE
# 30
# Invalid input





