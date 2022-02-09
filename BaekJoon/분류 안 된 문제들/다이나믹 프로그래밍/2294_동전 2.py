import sys
sys.stdin = open("2294_동전 2.txt", "rt")


def solution(k, coins):
    dp = [float('inf')] * (k + 1)
    for coin in coins:
        if coin <= k:
            dp[coin] = 1

    for i in range(k + 1):
        for coin in coins:
            if i + coin <= k:
                dp[i + coin] = min(dp[i] + 1, dp[i + coin])

    return dp[k] if dp[k] != float('inf') else -1


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    print(solution(k, coins))
