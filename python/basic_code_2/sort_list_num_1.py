# a=['9','6','4','8','7','3','2','4','5','6']
# from builtins import print

a=[4,3,8,5]

print(a)

# a.sort()
# print(a)

b=[]

for i in a:
    min=i
    for j in a:
        if min>=j:
            min=j
    b.append(min)
    # a.remove(min)

print(b)


# print(b)