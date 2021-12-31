import sys
sys.stdin = open('1929_소수 구하기.txt', 'rt')


M, N = map(int, input().split())
for n in range(M, N+1):
    if n >= 2:
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                break
        else:
            print(n)