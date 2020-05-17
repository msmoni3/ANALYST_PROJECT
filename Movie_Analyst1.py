import csv

with open('file.csv', 'r', encoding='utf-8') as csv_file: ### Open the CSV File
    reader = csv.reader(csv_file)                         ### crating variable to read file as reader
    csv_headings = next(reader)                           ### Storing the Csv Header in variable
    print(csv_headings)
    i = 0
    while i < 5:
        row = next(reader)
        print(row)
        i = i + 1

    with open('file_without_header.csv' , 'w' ,encoding='utf-8' ) as csv_file1:
        writer = csv.writer(csv_file1)
        for rows in reader:
            writer.writerow(rows)

    with open('updated.csv' , 'w' ,encoding='utf-8' ) as csv_file2:
        writer = csv.writer(csv_file2)
        for rows in reader:
            if rows[2] != '4553':
                #print(rows)
                writer.writerow(rows)


csv_file.close()
