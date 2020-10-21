import sys
sys.stdin = open('11653_소인수분해.txt', 'rt')


N = int(input())

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N = int(N/i)
            break