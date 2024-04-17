# a=['9','6','4','8','7','3','2','4','5','6']
# from builtins import print

a=[4,3,8,5]

print(a)

# a.sort()
# print(a)

b=[]

for i in a:
    # print(i)
    # min=i
    # print(type(i))
    min=i
    for j in a:
        if j<min:
            min=j

        # else:
        #     min=min
    # print(type(min))
    b.append(min)
    a.remove(min)

print(b)


# print(b)