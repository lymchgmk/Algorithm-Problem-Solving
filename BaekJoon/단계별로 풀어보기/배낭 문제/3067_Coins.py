import sys
sys.stdin = open('3067_Coins.txt', 'rt')


def solution(N, COINS, M):
    dp = [1] + [0] * M
    for coin in COINS:
        for money in range(coin, M+1):
            dp[money] = dp[money] + dp[money - coin]
    return dp[M]


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        COINS = list(map(int, input().split()))
        M = int(input())
        print(solution(N, COINS, M))
