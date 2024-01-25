def solution(temperature, t1, t2, a, b, onboard):
    OFFSET = 11
    temperature, t1, t2 = temperature + OFFSET, t1 + OFFSET, t2 + OFFSET

    MAX_TEMPERATURE = 40 + OFFSET
    TIMES = len(onboard)
    INF = float('inf')
    dp = [[INF] * (MAX_TEMPERATURE + 1) for _ in range(TIMES)]
    dp[0][temperature] = 0

    for curr_time in range(1, TIMES):
        for curr_temp in range(1, MAX_TEMPERATURE):
            if curr_temp == temperature:
                dp[curr_time][curr_temp] = dp[curr_time - 1][curr_temp]
            else:
                dp[curr_time][curr_temp] = min(
                    dp[curr_time - 1][curr_temp - 1] + a,
                    dp[curr_time - 1][curr_temp + 1] + a,
                    dp[curr_time - 1][curr_temp] + b
                )

    for row in dp:
        print(row)

    print(dp[-1][t1: t2+1])


if __name__ == "__main__":
    temperature = 28
    t1 = 18
    t2 = 26
    a = 10
    b = 8
    onboard = [0, 0, 1, 1, 1, 1, 1]
    result = 40
    answer = solution(temperature, t1, t2, a, b, onboard)
    print(answer == result, answer)
