import sys
sys.stdin = open('2004_조합 0의 개수.txt', 'rt')


import math


n, m = map(int, input().split())
result = 1
for i in range(n, 0 ,-1):
    if i > n-m:
        print(i)
        result *= i
    elif i <= m:
        result //= i

count = 0
for s in str(result)[::-1]:
    if s == '0':
        count += 1
    else:
        break
print(count)