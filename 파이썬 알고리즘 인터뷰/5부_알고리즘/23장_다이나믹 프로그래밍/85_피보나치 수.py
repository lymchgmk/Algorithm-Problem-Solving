import collections
import numpy as np

# 풀이 1. 재귀 구조 브루트 포스
def fib_1(self, N: int) -> int:
    if N <= 1:
        return N
    return self.fib(N - 1) + self.fib(N - 2)


# 풀이 2. 메모이제이션
class Solution_2:
    dp = collections.defaultdict(int)
    
    def fib_2(self, N: int) -> int:
        if N <= 1:
            return N
        
        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]
    
    
# 풀이 3. 타뷸레이션
class Solution_3:
    dp = collections.defaultdict(int)
    
    def fibo_3(self, N: int) -> int:
        self.dp[1] = 1
        
        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]
    

# 풀이 4. 두 변수만 이용해 공간 절약
def fib_4(self, N: int) -> int:
    x, y = 0, 1
    for i in range(0, N):
        x, y = y, x + y
    return x


# 풀이 5. 행렬
def fib_5(self, N: int) -> int:
    M = np.matrx([0, 1], [1, 1])
    vec = np.array([[0], [1]])
    
    return np.matmul(M ** n, vec)[0]