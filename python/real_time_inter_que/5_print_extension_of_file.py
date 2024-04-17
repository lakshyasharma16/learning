filename = "abc.txt"

# print(filename[filename.find(".")+1::])
dot_location = filename.find(".")
print("dot_location : " + str(dot_location))

extension = filename[dot_location + 1::]
print("extension : " + extension)
