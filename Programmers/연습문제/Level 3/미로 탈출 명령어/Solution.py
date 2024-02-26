def solution(n, m, x, y, r, c, k):
    MAX_R, MAX_C, START, END, DIST = n, m, (x - 1, y - 1), (r - 1, c - 1), k
    UP, DOWN, LEFT, RIGHT = "u", "d", "l", "r"
    DIRS = {UP: (-1, 0), RIGHT: (0, 1), LEFT: (0, -1), DOWN: (1, 0)}
    IMPOSSIBLE = "impossible"

    if not reachable(START, END, DIST):
        return IMPOSSIBLE

    stack = [(START, "", DIST)]
    while stack:
        curr_pos, curr_path, curr_remain_dist = stack.pop()

        if is_answer(curr_pos, END, curr_remain_dist):
            return curr_path

        curr_r, curr_c = curr_pos
        for dir_path, (dir_r, dir_c) in DIRS.items():
            post_r, post_c, post_path, post_remain_dist = curr_r + dir_r, curr_c + dir_c, curr_path + dir_path, curr_remain_dist - 1
            post_pos = (post_r, post_c)

            if can_move(post_r, post_c, MAX_R, MAX_C, post_remain_dist) and reachable(post_pos, END, post_remain_dist):
                stack.append(((post_r, post_c), post_path, post_remain_dist))

    return IMPOSSIBLE


def reachable(pos, end, remain_dist):
    min_total_dist = abs(end[0] - pos[0]) + abs(end[1] - pos[1])

    return min_total_dist <= remain_dist and (remain_dist - min_total_dist) % 2 == 0


def can_move(pos_r, pos_c, max_r, max_c, remain_dist):
    return 0 <= pos_r < max_r and 0 <= pos_c < max_c and 0 <= remain_dist


def is_answer(pos, end, remain_dist):
    return pos == end and remain_dist == 0


if __name__ == "__main__":
    n = 3
    m = 4
    x = 2
    y = 3
    r = 3
    c = 1
    k = 5
    result = "dllrl"
    print(solution(n, m, x, y, r, c, k))
