def solution(n):
    if n<=2:
        return n
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 2
    for i in range(1, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]


n = 2
print(solution(n))