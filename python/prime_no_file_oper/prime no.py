no = 29

status = "true"
for i in range(2, no):
    if no % i == 0:
        # print("not prime")
        status = "false"
        break;

if status == "true":
    print("no is prime")
else:
    print("no is not prime")
