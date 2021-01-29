import sys
sys.stdin = open('2609_최대공약수와 최소공배수.txt', 'rt')


N, M = map(int, input().split())

if max(N, M) % min(N, M) == 0:
    GCD, LCM = min(N, M), max(N, M)
else:
    GCD = 1
    for i in range(2, min(N, M)):
        if N % i == 0 and M % i == 0:
            GCD = i
    LCM = int(N*M/GCD)
print(GCD)
print(LCM)

