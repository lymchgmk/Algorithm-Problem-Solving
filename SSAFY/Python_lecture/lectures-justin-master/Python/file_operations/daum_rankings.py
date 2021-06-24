from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import csv

daum_url = 'https://www.daum.net/'

response = requests.get(daum_url).text
# print(response)
data = bs(response, 'html.parser')
# print(data)

rankings = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_mini > ol > li> div > div > span.txt_issue > a')
# print(rankings)

ranking_dict = {}
ranking_list = []

for idx, ranking in enumerate(rankings, start=1):
    # print(f'{idx}위 : {ranking.text}')
    # ranking_dict[f'{idx}위'] = ranking.text
    ranking_dict = {'rank': f'{idx}위', 'ranker': ranking.text}
    ranking_list.append(ranking_dict)

# pprint(ranking_list)

with open('daum_rank.csv', 'w', encoding='utf-8', newline='') as csvfile:
    # csv_writer = csv.writer(csvfile)
    #1. 저장할 데이터의 필드 이름을 미리 지정한다. 
    fieldnames = ('rank', 'ranker')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #2. 필드 이름을 csv 최상단에 작성한다.
    writer.writeheader()

    for ranking in ranking_list:
        # ranking -> dict
        writer.writerow(ranking)