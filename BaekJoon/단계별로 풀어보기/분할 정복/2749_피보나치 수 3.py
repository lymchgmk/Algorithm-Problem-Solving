import sys
sys.stdin = open("2749_피보나치 수 3.txt", "rt")


input = lambda: sys.stdin.readline().strip()
N = int(input())


def fibo(N):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]


    def square_matrix_mul(a, b, size=SIZE):
        new_matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new_matrix[i][j] += a[i][k]*b[k][j]

        return new_matrix

    
    def get_nth(N):
        matrix = ZERO.copy()
        tmp = BASE.copy()
        k = 0
        while 2**k <= N:
            if N & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)
        
        return matrix
    

    return get_nth(N)[1][0]


N %= 1500000
print(fibo(N)%1000000)