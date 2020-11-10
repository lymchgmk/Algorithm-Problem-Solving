import sys
sys.stdin = open("2156_포도주 시식.txt", 'rt')


input = sys.stdin.readline
n = int(input())
wine = [0] + [int(input()) for _ in range(n)]
dp = [0] + [0]*n
for i in range(1, n+1):
    if i <= 2:
        dp[i] = sum(wine[1: i+1])
    else:
        dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])

print(dp[n])
    
