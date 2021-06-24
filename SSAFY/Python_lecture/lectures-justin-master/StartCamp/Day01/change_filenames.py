import os

#1. 디렉토리 이동
os.chdir(r'C:\Users\multicampus\mygumi\StartCamp\dummy')

#2. 지정된 디렉토리 안에 있는 모든 파일 목록을 리스트로 반환
filenames = os.listdir('')
# print(type(filenames))

#3. 해당 리스트에서 파일을 하나씩 for문으로 꺼내 SAMSUNG_를 붙여준다.
for filename in filenames:
    # print(filename)
    os.renames(filename, filename.replace('SAMSUNG_SAMSUNG_', ''))