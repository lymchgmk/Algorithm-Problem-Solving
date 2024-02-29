NUMBER_PAD = [
    ('1', '2', '3'),
    ('4', '5', '6'),
    ('7', '8', '9'),
    ('*', '0', '#')
]

CACHED_POS = {}
NO_MOVE, UDLR_MOVE, DIA_MOVE = 1, 2, 3
INF = float('inf')


def solution(numbers):
    thumb_l, thumb_r = [1, 0], [1, 2]
    total_time = 0
    number_count, max_number_count = 0, len(numbers)
    stack = [(thumb_l, thumb_r, total_time, number_count)]
    total_time = INF
    while stack:
        curr_thumb_l, curr_thumb_r, curr_total_time, curr_number_count = stack.pop()

        if curr_number_count == max_number_count:
            total_time = min(total_time, curr_total_time)
            continue

        target_number = numbers[curr_number_count]
        target_position = calc_number_position(target_number, NUMBER_PAD)

        if target_position == curr_thumb_l or target_position == curr_thumb_r:
            stack.append((curr_thumb_l, curr_thumb_r, curr_total_time + NO_MOVE, curr_number_count + 1))
            continue

        time_l, time_r = calc_time(curr_thumb_l, target_position), calc_time(curr_thumb_r, target_position)
        if time_l < time_r:
            stack.append((target_position, curr_thumb_r, curr_total_time + time_l, curr_number_count + 1))
        elif time_l > time_r:
            stack.append((curr_thumb_l, target_position, curr_total_time + time_r, curr_number_count + 1))
        else:
            stack.append((target_position, curr_thumb_r, curr_total_time + time_l, curr_number_count + 1))
            stack.append((curr_thumb_l, target_position, curr_total_time + time_r, curr_number_count + 1))

    return total_time


def calc_number_position(number: str, pad: [[str]]) -> (int, int):
    if number in CACHED_POS:
       return CACHED_POS[number]

    for r in range(len(pad)):
        for c in range(len(pad[0])):
            if pad[r][c] == number:
                CACHED_POS[number] = (r, c)
                return r, c


def calc_time(thumb_pos, target_pos):
    diff_r, diff_c = abs(thumb_pos[0] - target_pos[0]), abs(thumb_pos[1] - target_pos[1])

    if diff_r == 0 and diff_c == 0:
        return NO_MOVE
    elif diff_r == 0 or diff_c == 0:
        return max(diff_r, diff_c) * UDLR_MOVE
    else:
        _dia = min(diff_r, diff_c)
        return _dia * DIA_MOVE + (max(diff_r, diff_c) - _dia) * UDLR_MOVE


if __name__ == "__main__":
    numbers = "5123"
    result = 8
    print(solution(numbers))
