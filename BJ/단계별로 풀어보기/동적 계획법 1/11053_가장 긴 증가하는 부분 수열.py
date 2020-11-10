import sys
sys.stdin = open("11053_가장 긴 증가하는 부분 수열.txt", 'rt')


input = sys.stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
dp = [1]*(N)
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))