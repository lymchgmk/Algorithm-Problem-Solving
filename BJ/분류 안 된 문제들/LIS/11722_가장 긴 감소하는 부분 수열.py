import sys
sys.stdin = open('11722_가장 긴 감소하는 부분 수열.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))

dp = [1]*N
for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
