from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

#1. api key와 url 세팅
api_key = 'TrrFpaTl72%2Bd1anFjwmpnPChTZFymdU84V5J9JzLqaF%2Fo2s4qsGgKVqjorobn05e16cjrneFsWc57BtIgPs%2BJw%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&numOfRows=40&pageNo=1&startPage=3&sidoName=%EA%B2%BD%EB%B6%81&ver=1.6'

#2. 현재 날짜 정보 활용 
diff = timedelta(hours=9)
today = datetime.now() + diff

#3. 요청을 보낸 응답 결과를 text로 저장하자 
response = requests.get(url).text

#4. 데이터를 구조화 시켜서 파이썬이 이해할 수 있는 형태로 변환하자
data = BeautifulSoup(response, 'html.parser')
# print(data)

#5. list에서 인덱싱 접근을 통해 값을 추출하자.(xml은 .find_all 활용)
items = data.find_all('item')
# print(items)
location = items[4]

#6. 미세먼지 데이터를 추출하자
dust = int(location.pm10value.text)
# print(dust)

#7. 측정소 정보를 추출하자
station = location.stationname.text
# print(station)

#8. 미세먼지 분기 코드 
if dust > 150:
    dust_rate = '매우 나쁨'
elif 80 < dust <= 150:
    dust_rate = '나쁨'
elif 30 < dust <= 80:
    dust_rate = '보통'
else:
    dust_rate = '좋음'

print(f'{station}의 {today.month}월 {today.day}일의 미세먼지 농도는 {dust}로 {dust_rate}입니다.')