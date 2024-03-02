NUMBER_PAD = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (None, 0, None)
)
MAX_NUMBER_PAD_R, MAX_NUMBER_PAD_C = len(NUMBER_PAD), len(NUMBER_PAD[0])
ALL_NUMBERS = range(10)
START_LEFT_THUMB, START_RIGHT_THUMB = 4, 6
CACHED_POSITION, CACHED_DISTANCE = {}, {}
NO_MOVE_WEIGHT, UDLR_MOVE_WEIGHT, DIA_MOVE_WEIGHT = 1, 2, 3
INF = float('inf')


def solution(numbers: str) -> int:
    dp = [[[INF for _ in ALL_NUMBERS] for _ in ALL_NUMBERS] for _ in range(len(numbers) + 1)]
    dp[0][START_LEFT_THUMB][START_RIGHT_THUMB] = 0

    for length, number in enumerate(map(int, numbers), start=1):
        for left_thumb in ALL_NUMBERS:
            for right_thumb in ALL_NUMBERS:
                if left_thumb == right_thumb:
                    continue

                if dp[length - 1][left_thumb][right_thumb] == INF:
                    continue

                dp[length][number][right_thumb] = min(
                    dp[length][number][right_thumb],
                    dp[length - 1][left_thumb][right_thumb] + calc_distance(left_thumb, number)
                )
                dp[length][left_thumb][number] = min(
                    dp[length][left_thumb][number],
                    dp[length - 1][left_thumb][right_thumb] + calc_distance(right_thumb, number)
                )

    return min(map(min, dp[-1]))


def calc_number_position(number: int) -> (int, int):
    if number in CACHED_POSITION:
        return CACHED_POSITION[number]

    for r in range(MAX_NUMBER_PAD_R):
        for c in range(MAX_NUMBER_PAD_C):
            if NUMBER_PAD[r][c] == number:
                CACHED_POSITION[number] = (r, c)
                return CACHED_POSITION[number]


def calc_distance(thumb: int, target: int) -> int:
    thumb_pos, target_pos = calc_number_position(thumb), calc_number_position(target)
    if (thumb_pos, target_pos) in CACHED_DISTANCE:
        return CACHED_DISTANCE[(thumb_pos, target_pos)]

    diff_r, diff_c = abs(thumb_pos[0] - target_pos[0]), abs(thumb_pos[1] - target_pos[1])
    if diff_r == 0 and diff_c == 0:
        _distance = NO_MOVE_WEIGHT
    elif diff_r == 0 or diff_c == 0:
        _distance = max(diff_r, diff_c) * UDLR_MOVE_WEIGHT
    else:
        _dia = min(diff_r, diff_c)
        _distance = _dia * DIA_MOVE_WEIGHT + (max(diff_r, diff_c) - _dia) * UDLR_MOVE_WEIGHT

    CACHED_DISTANCE[(thumb_pos, target_pos)] = _distance
    return _distance


if __name__ == "__main__":
    numbers = "5123"
    result = 8
    print(solution(numbers))
