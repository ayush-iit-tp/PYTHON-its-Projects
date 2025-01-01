# Dictionary & METHODS

# b = {}
#
# a=set() # To make empty set
#
# print(b, type(b))
# print(a, type(a))

 #        KEY : VALUE
marks = {"Harry": 69,
         "Hermione": 89,
         "Ron": 67,
         "Henry": 77}
# print(marks)
# print(marks["Harry"])

# TO ADD NEW KEYS
marks["Priyanka"] = 56
# print(marks)
#
# print(marks["Ayush"])
# # will give error
# print(marks.get("Ayush"))
# # will give none if key is not present
# print(marks.get("Harry"))

print(marks.keys())
print(marks.values())
print(marks.items())

# dict_keys(['Harry', 'Hermione', 'Ron', 'Henry', 'Priyanka'])
# dict_values([69, 89, 67, 77, 56])
# dict_items([('Harry', 69), ('Hermione', 89), ('Ron', 67), ('Henry', 77), ('Priyanka', 56)])



































