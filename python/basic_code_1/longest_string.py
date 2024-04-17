from builtins import print

a = "sgdfgdfghd"
b = "sdfsgrggdfgdfgdfgdfg"


def length(x):
    count = 0
    for i in x:
        count = count + 1

    return count


print(length(a))
print(length(b))

if length(a) > length(b):
    print("a is the longest string")
else:
    print("b is the longest string")
