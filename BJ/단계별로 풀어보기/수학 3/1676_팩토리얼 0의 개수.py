import sys
sys.stdin = open('1676_팩토리얼 0의 개수.txt', 'rt')


import math


N = int(input())
N_factorial = math.factorial(N)
count = 0
for n in str(N_factorial)[::-1]:
    if n == '0':
        count += 1
    else:
        break
print(count)