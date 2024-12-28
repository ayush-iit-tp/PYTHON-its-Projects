import math

 BASICS

print("Hello World")
print(math.floor(3.65))
print(math.cos(3.65))
print(65+15)
a=1
b=3
c="This is Ayush"
d=3.67
print(a+b)
print(c)
print(type(d))

 STRING

str1 = "This is my 1st python string"
print(str1)
str2 = "this is my 1st python string"
print(str2.capitalize())
print(str2.find("this"))
print(str1.find("this"))
print(str1.upper())
print(str1.lower())

 LIST

items = ["harry",2,3]
print(items)
print(type(items))
items[0] = "MD"
print(items)

items[1] = "ALI"
print(items)

 TUPLE

tup1 = (1,2,3)
print(tup1)
print(type(tup1))
## tup1 [0] = 7
print(tup1)

 YOU CAN'T change value of any tuple

 DICTIONARY

dict1 ={}
print(type(dict1))
print(dict1)
dict1["Virat"] = 100
dict1["Sachin"] = 200
print(dict1)
print(dict1.get("Virat"))
print(dict1.items())
print(dict1.keys())

 LIST TYPECASTING INTO SET
 IN SET :"ITEMS will not repeat"

list1 = [1,2,3,4,4,1]
print(list1)
s1 = set(list1)
print(s1)

 OPERATORS

a = 5
b = 10
c = "Harry"
print(a+b)
print(a+b+c) # error
print(str(a)+ str(b)+ c) # also error WHY? 

a = "5"
b = '10'
c = "Harry"
print(a+b)
print(a+b+c)
print("10 - 5 is ", 10-5)
print("10 * 5 is ", 10*5)
print("10 / 5 is ", 10/5)
print("10 + 5 is ", 10+5)

 VARIABLE & Conditional

var = int(input())
print(var)
if (var >4) :
    print("Variable is greater")
elif(var==2):
    print("Variable is equal to two")   
else:
    print("Variable is smaller")


 LOOPS

for i in range(0,100): # will print till 99
    print(i)

for i in range(0,101):
    print(i)

i=0
while(i<101):
    print(i)
    i  = i+1
    
 Finding Average using function

 def average(num1,num2):
    avr = (num1+num2)/2
    return avr

 print(average(3,5))

 USE OF TRY Except

index = 69
try:
    print(index)

except Exception as e:
    print(e)

  HOW TO READ FILE

f=open("1.txt", "w")
f.write("You are a SuperHero.")
f.close()

f=open ("1.txt", "r")
content = f.read()
f.close()
print(content)








