import sys
sys.stdin = open('2581_소수.txt', 'rt')

M = int(input())
N = int(input())

sum, min = 0, float('inf')
for n in range(M, N+1):
    if n >= 2:
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                break
        else:
            sum += n
            if min > n:
                min = n

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
