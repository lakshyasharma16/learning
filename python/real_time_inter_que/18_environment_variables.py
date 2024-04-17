import os.path, time,datetime

file_path = "C:\\Users\\Lakshya_Sharma\\PycharmProjects\\pythonProject2\\practice\\3_current_date.py"


# print(os.environ)
# print(os.environ['HOMEPATH'])
# print(os.environ['PATH'])


print("Last modified: %s" % time.ctime(os.path.getmtime(file_path)))
print("Created: %s" % time.ctime(os.path.getctime(file_path)))


print(os.path.getmtime(datetime.date(time.ctime(os.path.getmtime(file_path)))))
# print(os.path.getctime(file_path))
