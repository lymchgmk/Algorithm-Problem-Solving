from collections import deque


def solution(maps):
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)

    start2lever = bfs(maps, start, lever)
    lever2end = bfs(maps, lever, end)

    if start2lever != -1 and lever2end != -1:
        return start2lever + lever2end

    return -1


def bfs(maps, start, end):
    MAX_R, MAX_C = len(maps), len(maps[0])
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = [[False] * MAX_C for _ in range(MAX_R)]
    counts = [[0] * MAX_C for _ in range(MAX_R)]
    deq = deque([start])
    visited[start[0]][start[1]] = True

    while deq:
        curr_r, curr_c = deq.popleft()

        if (curr_r, curr_c) == end:
            return counts[end[0]][end[1]]

        for dir_r, dir_c in dirs:
            post_r, post_c = curr_r + dir_r, curr_c + dir_c
            if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and maps[post_r][post_c] != 'X' and not visited[post_r][post_c]:
                visited[post_r][post_c] = True
                counts[post_r][post_c] = counts[curr_r][curr_c] + 1
                deq.append((post_r, post_c))

    return -1


if __name__ == "__main__":
    maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
    result = 16
    answer = solution(maps)
    print(f'[{answer == result}] {answer}')
