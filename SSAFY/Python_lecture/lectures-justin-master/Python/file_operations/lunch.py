import csv

lunch = {
    '교촌치킨': '054-577-1233',
    '굽네치킨': '054-123-1234',
    'BHC': '054-123-4321'
}

# csvfile = open('lunch.csv', 'w', encoding='utf-8', newline='')
# csv_writer = csv.writer(csvfile)

# for item, phone in lunch.items():
#     csv_writer.writerow((item, phone))
# csvfile.close()

with open('lunch.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for item, phone in lunch.items():
        csv_writer.writerow((item, phone))