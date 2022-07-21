import csv

with open('resources/username.csv') as f:
    reader = csv.reader(f)
    # print(len(reader.line_num))
    for row in range(4):
        if row == 3:
            print(row)
