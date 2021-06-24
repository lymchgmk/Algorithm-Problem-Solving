from bs4 import BeautifulSoup
import requests

response = requests.get('https://finance.naver.com/sise/').text
# print(response)

data = BeautifulSoup(response, 'html.parser')
# print(data)

kospi = data.select_one('#KOSPI_now')
print(f'오늘의 kospi 지수는 {kospi.text}')
