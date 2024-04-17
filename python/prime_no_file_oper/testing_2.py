import csv
import datetime
# from builtins import print

date=datetime.datetime.utcnow()
print(date)
date_1=date.strftime("%d%m%y")
print(date_1)

new_file = "/basics/filtered_data_2.csv"
file_path = "/basics/abc.csv"


file = open(file_path, mode='r')
csvfile = csv.reader(file)

file_1 = open(new_file, mode='w')
# file_1.truncate(0)

for lines in csvfile:
    age = lines[1]
    if int(age) >= 25:
        print(lines)
        file_1.write(str(lines) + "\n")

file.close()
file_1.close()