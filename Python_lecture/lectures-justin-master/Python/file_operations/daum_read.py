import csv

with open('daum_rank.csv', 'r', encoding='utf-8', newline='') as csvfile:
    fieldnames = ('rank', 'ranker')
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)

    for row in reader:
        # print(row)
        print(row['rank'], row['ranker'])