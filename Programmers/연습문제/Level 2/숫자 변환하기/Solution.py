def solution(x, y, n):
    MAX = 1_000_000
    INF = float("inf")
    dp = [INF] * (MAX + 1)
    dp[x] = 0

    for i in range(x, y):

        if dp[y] != INF:
            return dp[y]

        n1, n2, n3 = i + n, 2 * i, 3 * i

        if 0 <= n1 <= MAX and dp[i] + 1 < dp[n1]:
            dp[n1] = dp[i] + 1
        if 0 <= n2 <= MAX and dp[i] + 1 < dp[n2]:
            dp[n2] = dp[i] + 1
        if 0 <= n3 <= MAX and dp[i] + 1 < dp[n3]:
            dp[n3] = dp[i] + 1

    return dp[y] if dp[y] != INF else -1


if __name__ == "__main__":
    x = 2
    y = 5
    n = 4
    result = 2
    answer = solution(x, y, n)
    print(f"[{answer == result}] {answer}")
