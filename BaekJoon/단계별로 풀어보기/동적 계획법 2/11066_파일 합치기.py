import sys
sys.stdin = open("11066_파일 합치기.txt", "rt")
input = lambda: sys.stdin.readline().strip()


T = int(input())
for _ in range(T):
    K = int(input())
    chapter = list(map(int, input().split()))

    # [i, j] 구간 합 구하기 위해서 만듦
    s = [0] * (K+1)
    for i in range(K):
        s[i+1] = s[i] + chapter[i]

    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    for i in range(1, K):
        for j in range(1, K-i+1):
            dp[j][j+i] = float('inf')
            for k in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + (s[j+i] - s[j-1]))
    
    print(dp[1][K])