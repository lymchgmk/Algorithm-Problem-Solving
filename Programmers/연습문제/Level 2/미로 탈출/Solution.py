from collections import deque

INF = float('inf')
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solution(maps):
    MAX_R, MAX_C = len(maps), len(maps[0])

    def bfs(start, end):
        start_r, start_c, end_r, end_c = start[0], start[1], end[0], end[1]
        counts = [[INF] * MAX_C for _ in range(MAX_R)]
        counts[start_r][start_c] = 0
        dq = deque([[start_r, start_c, counts[start_r][start_c]]])
        while dq:
            curr_r, curr_c, curr_count = dq.popleft()

            if curr_r == end_r and curr_c == end_c:
                return curr_count

            for dir_r, dir_c in DIRS:
                post_r, post_c, post_count = curr_r + dir_r, curr_c + dir_c, curr_count + 1
                if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and maps[post_r][post_c] != 'X' and post_count < counts[post_r][post_c]:
                    counts[post_r][post_c] = post_count
                    dq.append([post_r, post_c, post_count])

        return -1


    start, lever, end = [0, 0], [0, 0], [0, 0]
    for r in range(MAX_R):
        for c in range(MAX_C):
            if maps[r][c] == 'S':
                start = [r, c]
            elif maps[r][c] == 'L':
                lever = [r, c]
            elif maps[r][c] == 'E':
                end = [r, c]

    start_to_lever = bfs(start, lever)
    lever_to_end = bfs(lever, end)

    return start_to_lever + lever_to_end if (start_to_lever != -1 and lever_to_end != -1) else -1


if __name__ == "__main__":
    maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
    result = 16
    answer = solution(maps)
    print(f'[{answer == result}] {answer}')
