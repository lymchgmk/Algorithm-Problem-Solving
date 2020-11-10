import sys
sys.stdin = open("2565_전깃줄.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()

dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if AB[i][1] > AB[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))