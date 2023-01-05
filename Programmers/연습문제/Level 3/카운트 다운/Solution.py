def solution(target):
    INF = float('inf')
    dp = [[INF, 0] for _ in range(target + 1)]
    dp[0][0] = 0

    darts = range(1, 21)
    single_or_bull = [dart for dart in darts] + [50]
    double_or_triple = [2 * dart for dart in darts] + [3 * dart for dart in darts]

    for curr in range(target):
        for dart in single_or_bull:
            if curr + dart <= target and (dp[curr][0] + 1 < dp[curr + dart][0] or (dp[curr][0] + 1 == dp[curr + dart][0] and dp[curr][1] + 1 > dp[curr + dart][1])):
                dp[curr + dart][0] = dp[curr][0] + 1
                dp[curr + dart][1] = dp[curr][1] + 1

        for dart in double_or_triple:
            if curr + dart <= target and dp[curr][0] + 1 < dp[curr + dart][0]:
                dp[curr + dart][0] = dp[curr][0] + 1
                dp[curr + dart][1] = dp[curr][1]

    return dp[-1]


if __name__ == "__main__":
    target = 58
    print(solution(target))  # [2, 2]
