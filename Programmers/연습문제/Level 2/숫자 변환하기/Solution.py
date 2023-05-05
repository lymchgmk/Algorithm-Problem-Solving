MAX = 1_000_000
INF = float('inf')


def solution(x, y, n):
    dp = [INF] * (MAX + 1)
    dp[x] = 0

    for i in range(x, y):
        if dp[y] != INF:
            return dp[y]

        for new_n in (i + n, 2 * i, 3 * i):
            if MAX < new_n:
                continue

            dp[new_n] = min(dp[new_n], dp[i] + 1)

    return dp[y] if dp[y] != INF else -1


if __name__ == "__main__":
    x = 2
    y = 5
    n = 4
    result = 2
    answer = solution(x, y, n)
    print(f"[{answer == result}] {answer}")
