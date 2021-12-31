import sys
sys.stdin = open('11055_가장 큰 증가 부분 수열.txt', 'rt')


N = int(input())
A = list(map(int, input().split()))
dp = A.copy()

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
