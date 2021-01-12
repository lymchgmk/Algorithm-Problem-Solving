# Dict -> CSV 변환하는 3가지 방법 

lunch = {
    '교촌치킨': '054-577-1233',
    '굽네치킨': '054-123-1234',
    'BHC': '054-123-4321'
}

#1. String formatting 
with open('csv_conversion.csv', 'w', encoding='utf-8', newline='') as f:
    for key, value in lunch.items():
        f.write(f'{key}, {value}\n')

#2. join method 
with open('csv_conversion.csv', 'w', encoding='utf-8', newline='') as f:
    for item in lunch.items():
        f.write(', '.join(item)+'\n')

#3. csv.writer
import csv

with open('csv_conversion.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)