no = 153
new_no = 0
# for i in no:
#     new_no=i*i*i+new_no

# print(no%10)
while (no > 0):
    n = no % 10
    new_no = n * n * n + new_no
    # new_no=pow(n,3)+new_no
    no = int(no / 10)
    # print(n+" "+new_no+" "+no)
    print("{} {} {}".format(n, new_no, no))
print(new_no)
