no=123456789

sum=0

# for i in range(0:len(no)):
while(no>0):
    n=no%10
    sum=sum+n
    no=int(no/10)
    print(n)

print(sum)