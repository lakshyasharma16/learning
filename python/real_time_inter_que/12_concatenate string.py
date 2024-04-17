# Write a Python program that concatenates all elements in a list into a string and returns it.

string = "my name is lakshya"

list = []
for i in string:
    # if i not in list and i!= " ":
    if i not in list:
        list.append(i)

print(list)
