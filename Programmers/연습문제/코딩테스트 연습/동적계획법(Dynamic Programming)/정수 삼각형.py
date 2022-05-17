import copy


def solution(triangle):
    dp = triangle
    for i in range(1, len(dp)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] += dp[i-1][0]
            elif j == i:
                dp[i][j] += dp[i-1][i-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
            
    return max(dp[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))