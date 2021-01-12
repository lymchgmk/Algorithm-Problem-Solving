from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
melon_url = 'https://www.melon.com/chart/index.htm'

response = requests.get(melon_url, headers=headers).text
data = bs(response, 'html.parser')
songs = data.select('#lst50')
# print(songs)
# print(response)

result_list = []

for song in songs:
    # print(song)
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artists = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    # print(f'{rank}위 : {title} / {artist}')

    result_dict = {'rank': rank, 'title': title, 'artists': [artist.text for artist in artists]}
    result_list.append(result_dict)

# pprint(result_list)

with open('melon_rak.csv', 'w', encoding='utf-8', newline='') as csvfile:
    #1. csv에 들어 갈 cloumn 준비 - dictionary의 key와 일치해야 한다.
    fieldnames = ('rank', 'title', 'artists')

    #2. (실제) csv 필드 이름 작성
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 실제 컬럼 작성
    writer.writeheader()

    #3. 각 컬럼(필드)에 맞게 csv 데이터 저장(row)
    for item in result_list:
        writer.writerow(item)