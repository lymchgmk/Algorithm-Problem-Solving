import sys
sys.stdin = open("2579_계단 오르기.txt", 'rt')


input = sys.stdin.readline
N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N+1)
dp[1] = stairs[1]
dp[2] = dp[1] + stairs[2]
for i in range(3, N+1):
    dp[i] = stairs[i] + max(max(dp[i-1], dp[i-3]), max(dp[i-2],dp[i-3]))

print(dp)

