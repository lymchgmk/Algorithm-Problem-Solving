import sys
sys.stdin = open("11066_파일 합치기.txt", "rt")
input = lambda: sys.stdin.readline().strip()


T = int(input())
for _ in range(T):
    K = int(input())
    chapter = list(map(int, input().split()))

    dp = [[0]*K for _ in range(K)]
    for i in range(K-1):
        dp[i][i+1] = chapter[i] + chapter[i+1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + chapter[j]

    for i in range(2, K):
        for j in range(K-i):
            p_sum = [dp[j][k] + dp[k+1][j+i] for k in range(j, j+i)]
            dp[j][j+i] += min(p_sum)
    
    print(dp[0][K-1])