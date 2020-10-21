import sys
sys.stdin = open('3036_링.txt', 'rt')


import math


N = int(input())
R = list(map(int, input().split()))
for r in R[1:]:
    GCD = math.gcd(R[0], r)
    print(f'{int(R[0]/GCD)}/{int(r/GCD)}')