from flask import Flask, render_template, request
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, World!'
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2020, 5, 29)
    td = endgame - today
    return f'SSAFY 종료까지 {td.days}일 남았습니다.'

# /introduce -> 안녕하세요 ooo입니다. 
@app.route('/introduce')
def introdcue():
    return '안녕하세요. 김재석입니다.'

@app.route('/html')
def html():
    return '<h1>This is html h1 tag!</h1>'

@app.route('/html2')
def html2():
    return """
    <h1>This is html h1 tag!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다. {name}님!'
    return render_template('greeting.html', html_name=name)

# /cube/3 -> 3의 세제곱은 27입니다.
@app.route('/cube/<int:num>')
def cube(num):
    result = num**3
    return f'{num}의 세제곱은 {result}입니다.'

@app.route('/test')
def test():
    return 'test justin'

@app.route('/movie')
def movie():
    movies = ['한국영화', '홍콩영화', '미국영화']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    print(request)
    print(request.args)
    age = request.args.get('age')
    return render_template('pong.html', age=age)

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    check = 0
    if name.isdigit() == False:
        check = 1
    characters = ['똘끼', '순수함', '멍청함', '귀찮음', '돈', '건강', '재력', '먹을복', '사랑', '운']
    first = ['을 조금 넣어볼까?', ' 조금만', ' 한 스푼', '을 한 스푼~']
    second = [' 3스푼 넣고', ' 5스푼 넣고', '도 넣어주고~', '을 한스푼 넣어주자', '도 조금 있으면 좋겠군!']
    third = ['도 조금 넣어주자', '을 조그...으어ㅓㅓㅓ아ㅏㅏㅏ', '을 74컵 넣어주면 되겠군', '을 마지막으로 엌 바닥에 쏟았네;;']
    random_char = random.sample(characters, 3)
    random_first = random.choice(first)
    random_second = random.choice(second)
    random_third = random.choice(third)        
    return render_template('godmademe.html',name=name, chars=random_char, first=random_first, second=random_second, third=random_third, check=check)

@app.route('/dust')
def dust():
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

    return render_template(
        'dust.html', dust=dust, station=station, dust_rate=dust_rate, today=today
    )


if __name__ == '__main__':
    app.run(debug=True)