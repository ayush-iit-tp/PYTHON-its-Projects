# Context Managers
with open('example.txt', 'w') as f:
    f.write('Hello World!')
'''
File Handling with Context Managers
No need to explicitly close the file
'''

'''
Without Context Manager
you have to close the file
'''

'''
def error_func():
    file = open('file.txt', 'w')
    file.write('Hello')
    raise Exception()
    file.close()
'''











