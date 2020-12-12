import sys
sys.stdin = open("10842_팰린드롬!.txt", "rt")
input = lambda: sys.stdin.readline().strip()


N = int(input())
NUM = list(map(int, input().split()))
M = int(input())

dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if NUM[i] == NUM[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):
    for j in range(N-i):
        if NUM[j] == NUM[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

for _ in range(M):
    S, E = map(lambda x: int(x)-1, input().split())
    print(dp[S][E])
