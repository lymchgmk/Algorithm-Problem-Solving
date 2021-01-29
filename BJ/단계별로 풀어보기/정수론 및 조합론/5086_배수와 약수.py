import sys
sys.stdin = open('5086_배수와 약수.txt', 'rt')

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    else:
        if M/N == M//N:
            print('factor')
        elif N/M == N//M:
            print('multiple')
        else:
            print('neither')