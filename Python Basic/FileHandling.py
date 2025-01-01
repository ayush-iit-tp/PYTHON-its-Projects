# FILE HANDLING

s = "Ayush is a coder.He can code C, Python, Verilog too.!"

# WRITING TO A FILE

# USE THIS
# with open("test.txt", "w") as f:
#     f.write(s)

# OR USE THIS

# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()

# READING TO A FILE

# USE THIS
# with open("test.txt", "r") as f:
#    data = f.read()
#    print(data)

# OR USE THIS

fp = open("test.txt", "r")
data = fp.read()
print(data)
fp.close()














































