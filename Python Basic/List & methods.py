# LIST can be modified but strings can't

l1 = [1, 343, 2, 5661, 765, "Ayush"]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

print(l1)
print(type(l1))
l1.remove("Ayush")
print("New List is ",l1)

l1.sort()
print("Sorted List is ",l1)

l1.pop()
print("Popped List is ",l1)

l1.append("Ayush")
print("New List is ",l1)

l1.extend(l2)
print("New List is ",l1)

l1.extend([25,625,1025])
print("New List is ",l1)

print(l1.index("Ayush"))



































