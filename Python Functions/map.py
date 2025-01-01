# MAP Function

strings = ["my", "smartphone", "samsung", "M51"]

lengths = map(len, strings)
appends = map(lambda x:x + "s", strings)

print(list(lengths))
'''
[2, 10, 7, 3]
'''
print(list(appends))
'''
['mys', 'smartphones', 'samsungs', 'M51s']
'''







