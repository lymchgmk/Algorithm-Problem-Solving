import requests

#1. 요청을 보내기 위한 준비 작업
token = '805457410:AAGhgJeP4X79yj8TKWsrr_shUYbvjMWEZUo'
app_url = f'https://api.telegram.org/bot{token}'
# print(app_url)

#2. getUpdates로 bot 정보를 최신화(json -> dict)
update_url = f'{app_url}/getUpdates'
# print(update_url)
response = requests.get(update_url).json()
# print(response)
# print(type(response))

#3. chat_id 가져오기 
chat_id = response.get('result')[0].get('message').get('from').get('id')
# print(chat_id)

#4. 브라우저/Script를 통해 진행했던 것과 동일한 주소로 요청을 날리자!
text = '오늘은 즐거운 금요일입니다.'

message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
print(requests.get(message_url)) 