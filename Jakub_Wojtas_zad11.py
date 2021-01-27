import xlsxwriter
workbook = xlsxwriter.Workbook('file.xlsx')
workbook.close()

import csv
with open('university.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'University'])
    filewriter.writerow(['Jan', 'UP'])
    filewriter.writerow(['Karol', 'UJ'])
    filewriter.writerow(['Anna', 'AGH'])

with open('university.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import pandas as pd
df = pd.read_csv('university.csv')
df.to_excel('file.xlsx')