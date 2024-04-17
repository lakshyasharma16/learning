import csv
import os

new_file = "/basics/filtered_data.csv"
file_path = "/basics/abc.csv"

file_1 = open(new_file, mode='a')
file_1.truncate(0)
# opening the CSV file
with open(file_path, mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        # print(lines)
        # print(lines[1])
        age = lines[1]
        # print(type(age))
        # age=int(age)
        # print(age)
        # print(type(age))

        # print(age.isnumeric())
        # print(age)
        if int(age) >= 25:
            # print(lines+"\\n")
            file_1.write(str(lines) + "\n")

# file_1.close()