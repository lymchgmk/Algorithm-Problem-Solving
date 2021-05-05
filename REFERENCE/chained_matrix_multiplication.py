d = [matrix_sizes[0][0]] + [num for _, num in matrix_sizes]


def minimum(M, d, i, j):
    minValue = float('inf')
    minK = 0
    for k in range(i, j):
        value = M[i][k] + M[k + 1][j]
        value += d[i - 1] * d[k] * d[j]
        if minValue > value:
            minValue = value
            minK = k
    return minValue, minK


def minmult(d):
    n = len(d) - 1
    M = [[-1] * (n + 1) for _ in range(n + 1)]
    P = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        M[i][i] = 0
    
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j], P[i][j] = minimum(M, d, i, j)
    return M, P