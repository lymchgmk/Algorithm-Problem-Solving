import sys
sys.stdin = open("1086_박성원.txt", "rt")
input = lambda: sys.stdin.readline().strip()

import math


def dfs(L, visit, rest):
    if visit == (1<<N) - 1:
        if rest == 0:
            return 1
        else:
            return 0
    
    if dp[visit][rest] != -1:
        return dp[visit][rest]
    
    for i in range(N):
        if visit & (1<<i) == 0:
            dp[visit][rest] += dfs(L + long[i], visit | (1<<i), (rest+rm[i][L]) % K)
    dp[visit][rest] += 1
    return dp[visit][rest]


N = int(input())
stack = [int(input()) for _ in range(N)]
long = [len(str(i)) for i in stack]
K = int(input())
dp = [[-1]*K for _ in range(1<<N)]
rm = [[-1]*sum(long) for _ in range(N)]
for i in range(N):
    for j in range(sum(long)):
        rm[i][j] = (stack[i] * 10**j) % K

temp = dfs(0, 0, 0)
F = math.factorial(N)
if temp == 0:
    print('0/1')
else:
    v = math.gcd(F, dp[0][0])
    print(f'{temp//v}/{F//v}')