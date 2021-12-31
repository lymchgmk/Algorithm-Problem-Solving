import sys
sys.stdin = open('7562_나이트의 이동.txt', 'rt')
from collections import deque


T = int(input())
for _ in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    board = [[0]*l for _ in range(l)]
    deq = deque()

    deq.append([start_x, start_y, 0])

    dirs = ((-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2))

    while deq:
        pop_x, pop_y, pop_cnt = deq.popleft()

        if pop_x == end_x and pop_y == end_y:
            break

        for dir in dirs:
            dir_x, dir_y = dir
            if 0 <= pop_x + dir_x < l and 0 <= pop_y + dir_y < l and board[pop_x + dir_x][pop_y + dir_y] == 0:
                deq.append([pop_x + dir_x, pop_y + dir_y, pop_cnt + 1])
                board[pop_x + dir_x][pop_y + dir_y] = pop_cnt + 1

    print(board[end_x][end_y])

