import sys
sys.sydin=open('모의_별자리.txt')

T=int(input())

for test_case in range(1, T+1):
    data=[]
    for _ in range(T):
        data.append(list(map(int, input().split())))

    print(data)