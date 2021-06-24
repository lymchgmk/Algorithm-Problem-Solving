#1. split 
# with open('lunch.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     # print(lines)

#     for line in lines:
#         # print(line)
          # strip()은 파라미터가 주어지지 않으면 공백 + 개행 문자를 제거한다.
#         print(line.strip().split(','))

#2. csv.reader
import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)

    for item in items:
        print(item)