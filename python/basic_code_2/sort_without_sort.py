a=['9','6','4','8','7','3','2','4','5','6']

b=[]
for i in a:
    min=i
    for j in a:
        if min>=j:
            min=j
    b.append(min)
    a.remove(min)
    # print(i+" count is : "+ str(count))
print(b)

