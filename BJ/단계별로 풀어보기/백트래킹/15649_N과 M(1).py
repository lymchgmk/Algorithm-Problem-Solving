import sys
sys.stdin = open('15649_N과 M(1).txt', 'rt')


N, M = map(int, input().split())
for n in range(1, N+1):
    print(n)