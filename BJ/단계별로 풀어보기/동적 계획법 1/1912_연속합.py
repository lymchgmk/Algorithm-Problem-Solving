import sys
sys.stdin = open("1912_연속합.txt", 'rt')


input = sys.stdin.readline
n = int(input())
dp = list(map(int, input().split()))
for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1]+dp[i])

print(max(dp))