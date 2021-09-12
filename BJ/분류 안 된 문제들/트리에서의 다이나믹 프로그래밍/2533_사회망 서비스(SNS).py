import sys
sys.stdin = open("2533_사회망 서비스(SNS).txt", "r")
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)


def solve(num):
    visited[num] = True
    dp[num][0] = 0
    dp[num][1] = 1
    for child in graph[num]:
        if not visited[child]:
            solve(child)
            dp[num][0] += dp[child][1]
            dp[num][1] += min(dp[child][0], dp[child][1])


N = int(input())
graph = {idx: [] for idx in range(1, N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = {idx: [0, 0] for idx in range(1, N+1)}
visited = {idx: False for idx in range(1, N+1)}
solve(1)
print(min(dp[1]))
