def solution(temperature, t1, t2, a, b, onboard):
    OFFSET, INF = 10, float('inf')
    MIN_TEMP, MAX_TEMP = -10 + OFFSET, 40 + OFFSET
    MAX_TIME = len(onboard)
    room_temp, outside_temp, passenger_min_temp, passenger_max_temp = temperature + OFFSET, temperature + OFFSET, t1 + OFFSET, t2 + OFFSET
    on_power, off_power = a, b

    dp = [[INF] * (MAX_TEMP + 1) for _ in range(MAX_TIME)]
    dp[0][room_temp] = 0

    for curr_time in range(0, MAX_TIME - 1):
        for target_temp in range(0, MAX_TEMP + 1):
            prev_time = curr_time - 1

            # off
            if target_temp == outside_temp:
                dp[curr_time][target_temp] = min(dp[curr_time][target_temp], dp[prev_time][target_temp])
            elif target_temp < outside_temp:
                post_temp = target_temp + 1
                if is_temp_in_range(post_temp, MIN_TEMP, MAX_TEMP):
                    dp[curr_time][post_temp] =
            elif target_temp > outside_temp:
                return



def is_temp_in_range(target_temp, min_temp, max_temp):
    return min_temp <= target_temp <= max_temp



# def solution(temperature, t1, t2, a, b, onboard):
#     OFFSET = 11
#     temperature, t1, t2 = temperature + OFFSET, t1 + OFFSET, t2 + OFFSET
#
#     MAX_TEMPERATURE = 40 + OFFSET
#     TIMES = len(onboard)
#     INF = float('inf')
#     dp = [[INF] * (MAX_TEMPERATURE + 1) for _ in range(TIMES)]
#     dp[0][temperature] = 0
#
#     for curr_time in range(1, TIMES):
#         for curr_temp in range(1, MAX_TEMPERATURE):
#             if curr_temp == temperature:
#                 dp[curr_time][curr_temp] = dp[curr_time - 1][curr_temp]
#             else:
#                 dp[curr_time][curr_temp] = min(
#                     dp[curr_time - 1][curr_temp - 1] + a,
#                     dp[curr_time - 1][curr_temp + 1] + a,
#                     dp[curr_time - 1][curr_temp] + b
#                 )
#
#     for row in dp:
#         print(row)
#
#     print(dp[-1][t1: t2+1])


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
