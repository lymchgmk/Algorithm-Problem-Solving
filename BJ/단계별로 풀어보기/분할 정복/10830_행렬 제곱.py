import sys
sys.stdin = open("10830_행렬 제곱.txt", "rt")


input = lambda: sys.stdin.readline().strip()
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def square_array(A):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        row = A[i]
        for j in range(N):
            col = [row[j] for row in A]
            for k in range(N):
                res[i][j] += row[k]*col[k]
                res[i][j] %= 1000
    return res


def mul_array(X, Y):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        row_X = X[i]
        for j in range(N):
            col_Y = [row_Y[j] for row_Y in Y]
            for k in range(N):
                res[i][j] += row_X[k]*col_Y[k]
                res[i][j] %= 1000
    return res


bin_B = bin(B)[2:]
squared_A = [A]
for _ in range(len(bin_B)-1):
    squared_A.append(square_array(squared_A[-1]))

answer = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            answer[i][j] = 1

for idx, bit in enumerate(bin_B[::-1]):
    if bit == '1':
        answer = mul_array(answer, squared_A[idx])

for i in range(N):
    print(*answer[i])