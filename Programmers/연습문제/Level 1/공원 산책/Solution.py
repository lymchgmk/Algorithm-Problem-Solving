DIRS = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}


def solution(park, routes):
    MAX_R, MAX_C = len(park), len(park[0])

    start_r, start_c = 0, 0
    for r in range(MAX_R):
        for c in range(MAX_C):
            if park[r][c] == 'S':
                curr_r, curr_c = r, c

    for route in routes:
        dir_char, dist = route.split(" ")
        dir_r, dir_c = DIRS[dir_char]
        dist = int(dist)

        post_r, post_c = curr_r, curr_c
        can_go_route = True
        for _ in range(dist):
            if not (0 <= post_r + dir_r < MAX_R and 0 <= post_c + dir_c < MAX_C and park[post_r + dir_r][post_c + dir_c] != 'X'):
                can_go_route = False
                break

            post_r += dir_r
            post_c += dir_c

        if can_go_route:
            curr_r, curr_c = post_r, post_c

    return [curr_r, curr_c]


if __name__ == "__main__":
    park = ["SOO", "OOO", "OOO"]
    routes = ["E 2", "S 2", "W 1"]
    result = [2, 1]
    answer = solution(park, routes)
    print(answer == result, answer)