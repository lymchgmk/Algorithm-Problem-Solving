def solution(N):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]
    
    # 두 행렬의 곱을 구함, O(log2 N)
    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += (a[i][k] * b[k][j]) % 1000000007
        return new
    
    # 기본 행렬을 N번 곱한 행렬을 만든다
    def get_nth(N):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()
        
        while 2 ** k <= N:
            if N & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)
        
        return matrix
    
    return get_nth(N + 1)[1][0] % 1000000007


n = 4
print(solution(n))