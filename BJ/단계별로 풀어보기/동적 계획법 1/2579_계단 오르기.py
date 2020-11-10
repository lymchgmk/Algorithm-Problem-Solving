import sys
sys.stdin = open("2579_계단 오르기.txt", 'rt')


input = sys.stdin.readline
N = int(input())
stair = [int(input()) for _ in range(N)]

dp = [0]*(N+1)
if N == 1:
    dp[1] = stair[0]
elif N == 2:
    dp[1] = stair[0]
    dp[2] = max(stair[0]+stair[1],stair[1])
elif N == 3:
    dp[1] = stair[0]
    dp[2] = max(stair[0]+stair[1],stair[1])
    dp[3] = max(stair[0]+stair[2],stair[1]+stair[2])
else:
    dp[1] = stair[0]
    dp[2] = max(stair[0]+stair[1],stair[1])
    dp[3] = max(stair[0]+stair[2],stair[1]+stair[2])  
    for i in range(3,N+1):
        dp[i] = max(dp[i-2] + stair[i-1] , dp[i-3] + stair[i-2] + stair[i-1])

print(dp[N])
