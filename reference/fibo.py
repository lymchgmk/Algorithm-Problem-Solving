# 기본 재귀적 풀이, O(N) = 2^N
def fibo_1(N):
    return fibo_1(N-1) + fibo_1(N-2) if N>=2 else N

# 반복적 풀이, O(N) = N
def fibo_2(N):
    if N < 2:
        return N
    
    a, b = 0, 1
    for _ in range(N-1):
        a, b = b, a+b
    return b


# 동적계획법 풀이
def fibo_3(N):
    # Index error 방지!
    if N < 2:
        return N
    
    cache = [0]*(N+1)
    cache[1] = 1
    for i in range(2, N+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[N]


# 재귀적 동적 계획법 풀이
def fibo_4(N):
    cache = [-1]*(N+1)

    def iterate(N):
        # 기저사례 1, 기저사례(base case): 재귀 함수가 끝나도록 하는 조건
        if N < 2:
            return N
        
        # 기저사례 2
        if cache[N] != -1:
            return cache[N]

        # 기저사례에 해당하지 않는 경우, 실제로 계산
        cache[N] = iterate(N-1) + iterate(N-2)
        return cache[N]

    return iterate(N)


# 파이썬 함수의 동작방식을 활용한 풀이
def fibo_5(N, __cache = {0: 0, 1: 1}):
    if N in __cache:
        return __cache[N]

    __cache[N] = fibo_5(N-1) + fibo_5(N-2)
    return __cache[N]


# 행렬 곱셈을 활용한 풀이, 빠른 방법
def fibo_6(N):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]]
    BASE = [[1, 1], [1, 0]]

    # 두 행렬의 곱을 구함, O(log2 N)
    def square_matrix_mul(a, b, size = SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]
        return new

    # 기본 행렬을 N번 곱한 행렬을 만든다
    def get_nth(N):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2**k <= N:
            if N & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)
        
        return matrix

    return get_nth(N)[1][0]


# 일반항 사용, O(log2 N)
def fibo_7(N):
    sqrt_5 = 5 ** (1/2)
    return int((1/sqrt_5) * (((1+sqrt_5)/2)**N - ((1-sqrt_5)/2)**N))

