import sys
sys.stdin = open('1904_01타일.txt', 'rt')


N = int(input())


def zero_one(n):
    if n <= 2:
        return dp[n]
    else:
        
dp = [0, 1, 2]
