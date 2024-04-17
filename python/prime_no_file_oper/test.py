import csv

new_file = "/basics/filtered_data.csv"

file_path = "/basics/abc.csv"

# with open(new_file, 'a')

with open(file_path, 'r'):
    values = csv.reader(file_path, delimiter=",")
    for i in values:
        print(i[0])
        # if i[1] > 25:
        #     print(i[0])
