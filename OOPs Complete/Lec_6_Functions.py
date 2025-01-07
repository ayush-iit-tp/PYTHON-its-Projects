#Printing length of any list using function

CU = ["MCU","MCU","KCU","DC","DC"]
heroes = ["Thor","IronMan","Krrish","Batman","Superman"]

def print_len(list):
    print("The number of the superheros are: ",
          len(list))

#print_len(CU)
print_len(heroes)

#WAF to print the elements of list in a single line
'''
print(heroes[0], end="|")
print(CU[0], end="||")
print(heroes[1], end="|")
print(CU[1], end="||")
print(heroes[2], end="|")
print(CU[2], end="||")
print(heroes[3], end="|")
print(CU[3], end="||")
print(heroes[4], end="|")
print(CU[4], end="||")
'''
#Using Loops to do it
def print_list(list):
    for hero in list:
        print(hero, end=" | ")

print_list(heroes)
print()

















































































