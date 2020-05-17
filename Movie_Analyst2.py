import csv

with open('file.csv' , 'r' ,encoding='utf-8') as csv_file1:
    reader = csv.reader(csv_file1)
    for rows in reader:
        
