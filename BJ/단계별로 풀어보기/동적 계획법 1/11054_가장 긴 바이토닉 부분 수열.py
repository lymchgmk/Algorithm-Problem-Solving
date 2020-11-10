import sys
sys.stdin = open("11054_가장 긴 바이토닉 부분 수열.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))

dp_fwd = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_fwd[i] = max(dp_fwd[i], dp_fwd[j] + 1)

dp_rev = [1]*N
for i in range(N-1 ,-1, -1):
    for j in range(N-1, i-1, -1):
        if A[i] > A[j]:
            dp_rev[i] = max(dp_rev[i], dp_rev[j] + 1)

result = [dp_fwd[i] + dp_rev[i] for i in range(N)]
print(max(result)-1)
