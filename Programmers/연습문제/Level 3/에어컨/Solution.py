OFFSET = 10 + 1
MIN_TEMP, MAX_TEMP = -10 + OFFSET, 40 + OFFSET + 1000 // 2
INF = float('inf')


def solution(temperature, t1, t2, a, b, onboard):
    outside_temp = temperature + OFFSET
    passenger_min_temp, passenger_max_temp, change_power, keep_power = t1 + OFFSET, t2 + OFFSET, a, b
    MAX_TIME = len(onboard)
    dp = [[INF] * (MAX_TEMP + 2) for _ in range(MAX_TIME + 1)]
    dp[0][outside_temp] = 0

    for curr_time in range(0, MAX_TIME):
        post_time = curr_time + 1
        inside_temp_range = range(1, MAX_TEMP + 1) if not is_passenger(post_time, onboard) else range(passenger_min_temp, passenger_max_temp + 1)
        for post_inside_temp in inside_temp_range:
            dp[post_time][post_inside_temp] = min(
                dp[curr_time][post_inside_temp - 1] if post_inside_temp - 1 < outside_temp else INF,
                dp[curr_time][post_inside_temp] if post_inside_temp == outside_temp else INF,
                dp[curr_time][post_inside_temp + 1] if post_inside_temp + 1 > outside_temp else INF,
                dp[curr_time][post_inside_temp] + keep_power,
                dp[curr_time][post_inside_temp - 1] + change_power, dp[curr_time][post_inside_temp + 1] + change_power
            )

    return min(dp[-1])


def is_passenger(time, onboard):
    return onboard[time - 1] == 1


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
