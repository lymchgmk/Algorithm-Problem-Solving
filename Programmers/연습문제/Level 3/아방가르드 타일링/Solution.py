def solution(n):
    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 3, 10

    for i in range(4, n+1):
        for j in range(1, i):
            k = i - j
            dp[i] += dp[j] * dp[k]
        dp[i] -= i

    return dp[n]


if __name__ == "__main__":
    n = 3
    result = 10
    answer = solution(n)
    print(answer == result , answer)
