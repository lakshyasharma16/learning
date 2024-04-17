string = "my name is lakshya"

prefix = "ls"

new_string = prefix + string

print("new_string after adding prefix:\t\t\t\t " + new_string)
# print(new_string[0:2])

if new_string[0:2] == "ls":
    print("new_string after removing the prefix :\t\t " + new_string[2::])
