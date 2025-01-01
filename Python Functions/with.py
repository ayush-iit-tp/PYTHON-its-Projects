with open("test.txt", "a") as file:
    file.write("\nI have appended Here.")
    # automatically closes the file
with open("test.txt", "r") as file:
    print(file.read())
'''
Practicing PYTHON Coding
Hello! I am AyushHere
Here
I have appended Here.
I have appended Here.
'''