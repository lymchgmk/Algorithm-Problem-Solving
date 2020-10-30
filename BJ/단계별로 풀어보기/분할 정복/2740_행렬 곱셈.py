import sys
sys.stdin = open("2740_행렬 곱셈.txt", "rt")


A_N, A_M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(A_N)]

B_M, B_K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(B_M)]

result = [[0 for _ in range(B_K)] for _ in range(A_N)]
for i in range(A_N):
    A_row = A[i]
    for j in range(B_K):
        B_col = [B_row[j] for B_row in B]
        for k in range(A_M):
            result[i][j] += A_row[k]*B_col[k]
        
for idx in range(A_N):
    print(*result[idx])