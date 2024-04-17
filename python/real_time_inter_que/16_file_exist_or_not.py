import os

file_path = "C:\\Users\\Lakshya_Sharma\\PycharmProjects\\pythonProject2\\practice\\3_current_date.py"

print(file_path)

status = os.path.exists(file_path)
print(status)

if status == True:
    data = open(file_path, "r")
    print(data.read())
