import sys
sys.stdin = open('1904_01타일.txt', 'rt')


input = sys.stdin.readline
N = int(input())
dp = [0, 1, 2] + [0]*(999999)
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])