#  json ->
#  txt ->
#  csv  ->
#
#
# name,grade,favfood
# gzal,99,mansaf
# israe,100,hamburger
# dvir,88,nuggets
# eli,,rice_and_lof

import csv

with open('employee.csv', 'r') as emp:
    csv_reader = csv.reader(emp, delimiter=',')
    line = 0
    grade_index= 0
    for row in csv_reader:
        if line != 0:
            print(row[grade_index])

        else:
            print(f'title {row}')
            for i in row:
                if i == 'grade':
                    grade_index= row.index(i)
        line += 1


with open('employee.csv', 'w') as emp:
    try:
        print(10/0)
        emp.read()
    except Exception as s:
        print(s)
