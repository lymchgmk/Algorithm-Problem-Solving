import sys
sys.stdin = open('11054_가장 긴 바이토닉 부분 수열', 'rt')


def LIS(arr):
    dp = [1]*N
    for i in range(N):
        for j in range(i):
            if arr[i] >  arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp


input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))
sub = LIS(A)
sub_rev = LIS(A[::-1])[::-1]
print(max(map(sum, zip(sub, sub_rev))) - 1)