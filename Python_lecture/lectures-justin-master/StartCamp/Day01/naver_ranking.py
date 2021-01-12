from bs4 import BeautifulSoup
import requests

#1. naver로 요청을 보내 text로 변환된 결과를 response 라는 변수에 담자!
response = requests.get('https://www.naver.com/').text
#2. BeautifulSoup을 활용해 응답 받은 문서를 이쁘게 만들어 보자!
data = BeautifulSoup(response, 'html.parser')
#3. selector를 활용해 실시간 검색어를 리스트로 받아 names라는 변수에 저장(할당)하자!
names = data.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')
# print(names)

for (idx, name) in enumerate(names):
    print(f'{idx+1}위: {name.text}')