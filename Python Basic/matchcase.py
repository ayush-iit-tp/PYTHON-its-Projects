# MATCH CASE
from unittest import case

a = int(input("Enter the first number: "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 23:
        print("Case is 23")
    case 33:
        print("Case is 33")
    case _:
        print("Case is unknown")











































