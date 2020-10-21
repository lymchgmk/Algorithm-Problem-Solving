import sys
sys.stdin = open('11051_이항 계수 2.txt', 'rt')


import math


N, K = map(int, input().split())
print(math.comb(N, K) % 10007)