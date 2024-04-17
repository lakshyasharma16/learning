#29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

list_1_len=len(color_list_1)
list_2_len=len(color_list_2)

new_list=[]

for i in color_list_1:
    for j in color_list_2:
        if i==j:
            new_list.append(i)

print(new_list)