import sys
sys.stdin = open('1149_RGB거리.txt', 'rt')


N = int(input())
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [houses[0]] + [[0, 0, 0] for _ in range(N-1)]
for i in range(1, N):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + houses[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + houses[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + houses[i][2]

print(min(DP[N-1]))