def check_prime(x):
    no = x
    state = "true"
    for i in range(2, no):
        if no % i == 0:
            # print("not prime")
            state = "false"
            break;
    return state


status = check_prime(7)
print(status)

if status == "true":
    print("no is prime")
elif status == "false":
    print("no is not prime")
