import sys
sys.stdin = open("1249_보급로.txt")

from collections import deque


def is_safe(node, N):
    return 0 <= node[0] < N and 0 <= node[1] < N


def lets_work(start, end, N, BATTLEFIELD):
    worked = [[-1 for _ in range(N)] for _ in range(N)]
    deq = deque([start])
    worked[start[0]][start[1]] = BATTLEFIELD[start[0]][start[1]]
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    while deq:

        x, y = deq.popleft()
        if [x, y] == end:
            continue

        for i in range(4):
            temp_x, temp_y = x+dirs[i][0], y+dirs[i][1]

            if not is_safe([temp_x, temp_y], N):
                continue

            if worked[temp_x][temp_y] == -1 or worked[x][y] + BATTLEFIELD[temp_x][temp_y] < worked[temp_x][temp_y]:
                worked[temp_x][temp_y] = worked[x][y] + BATTLEFIELD[temp_x][temp_y]
                deq.append([temp_x, temp_y])

    return worked[end[0]][end[1]]


T=int(input())
for test_case in range(1, T+1):
    N = int(input())
    BATTLEFIELD = [list(map(int, list(str(input())))) for _ in range(N)]

    start, end = [0, 0], [N-1, N-1]

    answer = lets_work(start, end, N, BATTLEFIELD)
    print(f'#{test_case} {answer}')