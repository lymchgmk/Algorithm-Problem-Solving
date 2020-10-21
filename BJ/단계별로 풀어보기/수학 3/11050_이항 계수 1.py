import sys
sys.stdin = open('11050_이항 계수 1.txt', 'rt')


import math


N, K = map(int, input().split())
answer = 1
for i in range(N, 0, -1):
    print(answer)
    if i > K:
        answer *= i
    else:
        answer /= i

print(answer)