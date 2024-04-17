a=['9','6','4','8','7','3','2','4','5','6']


for i in a:
    count=0
    for j in a:
        if i<=j:
            count=count+1
    a.remove(i)
    print(i+" count is : "+ str(count))