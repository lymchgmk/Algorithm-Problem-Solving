import sys
sys.stdin = open('1037_약수.txt', 'rt')


N = int(input())
divisor = sorted(list(map(int, input().split())))

if len(divisor) == 1:
    print(divisor[0] ** 2)
else:
    print(divisor[0] * divisor[N-1])
