import sys
sys.stdin = open("2293_동전 1.txt", "rt")


input = lambda: sys.stdin.readline().strip()
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [0]*10001
dp[0] = 1
for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

print(dp[k])
