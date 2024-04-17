# 45. Write a Python program that calls an external command.
file_path = "C:\\Users\\Lakshya_Sharma\\PycharmProjects\\pythonProject2\\practice\\3_current_date.py"

import os

print(os.system("dir"))

print(os.path.realpath(file_path))
