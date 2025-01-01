strings = ["my", "smartphone", "samsung", "M51"]

def add_s(string):
        return string +"s"

lengths = map(add_s, strings)
print(list(lengths))
'''
['mys', 'smartphones', 'samsungs', 'M51s']
'''