# FILTER FUNC

def longer_than_4(string):
    return len(string) > 4

strings = ["my", "smartphone", "samsung", "M51"]
filtered = filter(longer_than_4, strings)
print(list(filtered))
'''
['smartphone', 'samsung']
'''






