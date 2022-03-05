import sys
sys.stdin = open('9084_동전.txt', 'rt')


def solution(N, coins, M):
    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for money in range(coin, M+1):
            dp[money] = dp[money] + dp[money - coin]
    return dp[M]


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = map(int, input().split())
        M = int(input())
        print(solution(N, coins, M))
