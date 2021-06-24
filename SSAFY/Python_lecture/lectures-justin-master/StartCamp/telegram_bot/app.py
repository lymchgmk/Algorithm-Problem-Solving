from flask import Flask, render_template, request
from pprint import pprint
import requests

app = Flask(__name__)

# 요청을 위한 기본 준비
token = '805457410:AAGhgJeP4X79yj8TKWsrr_shUYbvjMWEZUo'
chat_id = '749251074'
naver_client_id = 'bej3naFebiOt4saB3r0h'
naver_client_secret = '2u4UN7QruP'

app_url = f'https://api.telegram.org/bot{token}'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    #1. 사용자가 보낸 메시지를 받아서 text 변수에 저장하자
    text = request.args.get('msg')

    #2. Telegram bot이 chat_id를 가진 사람에게 메시지를 보낸다.
    message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'

    #3. 텔레그램 서버로 메시지 전송
    requests.get(message_url)

    return render_template('send.html')

@app.route('/telegram', methods=['POST'])
def telegram():
    telegram_response = request.get_json()
    # pprint(telegram_response)
    # print(request)

    if telegram_response.get('message') is not None:
        chat_id = telegram_response.get('message').get('chat').get('id')
        text = telegram_response.get('message').get('text')
        # requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')

        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }

            data = {
                'source': 'ko',
                'target': 'ja',
                'text': text[4:]
            }

            papage_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt',
                headers=headers,
                data=data
            ).json()

            # pprint(papage_response)
            text = papage_response.get('message').get('result').get('translatedText')
        requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200


if __name__ == '__main__':
    app.run(debug=True)