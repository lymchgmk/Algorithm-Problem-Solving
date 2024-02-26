from copy import deepcopy


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX_R = MAX_C = 0


def solution(land):
    global MAX_R, MAX_C

    MAX_R, MAX_C = len(land), len(land[0])
    max_oil = 0
    for curr_c in range(MAX_C):
        curr_max_oil, curr_land = 0, deepcopy(land)
        for curr_r in range(MAX_R):
            curr_drilled_oil, curr_land = oil_drilling(curr_r, curr_c, curr_land)
            curr_max_oil += curr_drilled_oil

        max_oil = max(max_oil, curr_max_oil)

    return max_oil


def oil_drilling(r, c, land):
    global MAX_R, MAX_C

    if land[r][c] == 0:
        return 0, land

    oil = 0
    stack = [(r, c)]
    while stack:
        curr_r, curr_c = stack.pop()
        oil += land[curr_r][curr_c]
        land[curr_r][curr_c] = 0

        for dir_r, dir_c in DIRS:
            post_r, post_c = curr_r + dir_r, curr_c + dir_c

            if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and land[post_r][post_c] == 1:
                stack.append((post_r, post_c))

    return oil, land


if __name__ == "__main__":
    land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
    result = 9
    print(solution(land))