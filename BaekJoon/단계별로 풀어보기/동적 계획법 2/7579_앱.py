import sys
sys.stdin = open("7579_앱.txt", "rt")
input = lambda: sys.stdin.readline().strip()


N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
sum_C = sum(C)

dp_ks = [[0 for _ in range(sum_C+1)] for _ in range(N+1)]
result = sum_C
for i in range(1, N+1):
    byte, cost = A[i], C[i]
    for j in range(1, sum_C+1):
        if j < cost:
            dp_ks[i][j] = dp_ks[i-1][j]
        else:
            dp_ks[i][j] = max(byte + dp_ks[i-1][j-cost], dp_ks[i-1][j])
        
        if dp_ks[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else:
    print(0)
