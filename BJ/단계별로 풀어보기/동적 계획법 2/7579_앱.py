import sys
sys.stdin = open("7579_앱.txt", "rt")
input = lambda: sys.stdin.readline().strip()


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
C = list(map(int, input().split()))

dp_ks = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        w, v = C[i], A[i]
        if j < w:
            dp_ks[i][j] = dp_ks[i-1][j]
        else:
            dp_ks[i][j] = max(dp_ks[i-1][j-w] + v, dp_ks[i-1][j])

print(dp_ks)
