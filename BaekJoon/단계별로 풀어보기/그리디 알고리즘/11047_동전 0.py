import sys
sys.stdin = open('11047_동전 0.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)][::-1]

cnt = 0
for a in A:
    if K >= a:
        cnt += K//a
        K %= a
    if K == 0:
        break
print(cnt)