import sys
sys.stdin = open("2482_색상환.txt", "rt")
input = lambda: sys.stdin.readline().strip()

N = int(input())
K = int(input())

DP = [[0]*(N+1) for _ in range(N+1)]


def solve(n, k, dp):
    if n/k == 2:
        return 2

    if k == 1:
        return n

    if dp[n][k] == 0:
        dp[n][k] = solve(n-1, k, dp) + solve(n-2, k-1, dp)
        return dp[n][k]
    else:
        return dp[n][k]


if N/2 < K:
    print(0)
else:
    print(solve(N, K, DP)%1000000003)