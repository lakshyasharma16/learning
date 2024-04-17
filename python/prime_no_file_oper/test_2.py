str = "My name is Lakshya and I am a devops engineer"

# Print the words in this string which has even number of letters

list = str.split(" ")
# list=str.split["\ "]

for i in list:
    if int(len(i)) % 2 == 0:
        print(i)
