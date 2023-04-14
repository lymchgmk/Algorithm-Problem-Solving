DIV = 1_000_000_007


def solution(n, money):
    dp = [1] + [0] * n

    for coin in sorted(money):
        for price in range(coin, n+1):
            dp[price] = (dp[price] + dp[price - coin]) % DIV

    return dp[n]


if __name__ == "__main__":
    n = 5
    money = [1, 2, 5]
    result = 4
    answer = solution(n, money)
    print(result == answer, answer)
