# 네이버 금융에서 원/달러 환율 정보 크롤링 하기 
#1. 필요한 함수를 가져온다.
from bs4 import BeautifulSoup
import requests

#2. 요청을 보낸다.
response = requests.get('https://finance.naver.com/marketindex/').text

#3. 응답온 결과를 이쁘게(BeautifulSoup) 만들어 준다.
data = BeautifulSoup(response, 'html.parser')

#4. (이쁘게 만들어진 결과에서) selector를 활용해 정보를 뽑아낸다.
exchange = data.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')

#5. 원하는 데이터를 출력한다.
print(f'금일의 원/달러 환율은 {exchange.text}입니다.')