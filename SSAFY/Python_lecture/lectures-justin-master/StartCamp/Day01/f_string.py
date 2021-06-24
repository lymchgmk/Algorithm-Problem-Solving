import random

#1. 기본
name = '홍길동'
print(f'안녕하세요. {name}입니다.')
print('안녕하세요. ' + name + '입니다.')

# 점심 메뉴 추천(출력 결과를 f-string을 활용해 표현)
menu = ['피자', '치킨', '자장면', '짬뽕', '탕수육']
lunch = random.choice(menu)
print(f'오늘의 점심 메뉴는 {lunch}입니다.')

# 로또 번호 추천(출력 결과를 f-string을 활용해 표현)

lotto = random.sample(range(1, 46), 6)
print(lotto)