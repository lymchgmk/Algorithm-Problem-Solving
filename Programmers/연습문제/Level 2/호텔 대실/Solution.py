CLEAR_TIME_DELTA = 10


def solution(book_time):
    imos = [0] * (24 * 60 + 10)
    for start_time, end_time in book_time:
        start_minutes, end_minutes = time2minutes(start_time), time2minutes(end_time)
        imos[start_minutes] += 1
        imos[end_minutes + CLEAR_TIME_DELTA] -= 1

    cumulative_sum = 0
    max_rooms = 0
    for i in range(24 * 60):
        cumulative_sum += imos[i]
        max_rooms = max(max_rooms, cumulative_sum)

    return max_rooms


def time2minutes(time):
    HH, MM = map(int, time.split(":"))

    return HH * 60 + MM


if __name__ == "__main__":
    book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
    result = 3
    print(solution(book_time))
    print(solution(book_time) == result)