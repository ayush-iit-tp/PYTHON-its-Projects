def print_list(list,index=0):
    if index == len(list):
        return
    print(list[index],end=" | ")
    print_list(list,index+1)

heroes = ["Thor","IronMan","Krrish","Batman","Superman"]

print_list(heroes)