import os

dir_path = "C:\\Users\\Lakshya_Sharma\\PycharmProjects\\pythonProject2\\practice"

for i in os.listdir(dir_path):
    # print(i)
    # print(i[0:1])
    if True==i[0:1].isnumeric():
        print(i)