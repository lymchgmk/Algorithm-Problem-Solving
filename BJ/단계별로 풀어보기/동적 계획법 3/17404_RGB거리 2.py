import sys
sys.stdin = open("17404_RGB거리 2.txt", "rt")
input = lambda: sys.stdin.readline().strip()


N = int(input())
HOUSE = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')

ans = INF
for start_color in range(3):
    dp = [[0]*3 for _ in range(N)]
    for i in range(3):
        if i == start_color:
            dp[0][i] = HOUSE[0][i]
            continue
        else:
            dp[0][i] = INF

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + HOUSE[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + HOUSE[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + HOUSE[i][2]
    
    for i in range(3):
        if i != start_color:
            ans = min(ans, dp[-1][i])

print(ans)