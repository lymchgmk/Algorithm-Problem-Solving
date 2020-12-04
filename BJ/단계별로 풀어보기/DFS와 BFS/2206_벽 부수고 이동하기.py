import sys
sys.stdin = open('2206_벽 부수고 이동하기.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


def bfs():
    deq = deque([[0, 0, 1]])
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while deq:
        now_x, now_y, wall = deq.popleft()
        if now_x == N-1 and now_y == M-1:
            return visited[now_x][now_y][wall]
        for dir in dirs:
            next_x, next_y = now_x + dir[0], now_y + dir[1]
            if 0 <= next_x < N and 0 <= next_y < M:
                if arr[next_x][next_y] == 1 and wall == 1:
                    visited[next_x][next_y][0] = visited[now_x][now_y][1] + 1
                    deq.append([next_x, next_y, 0])
                elif arr[next_x][next_y] == 0 and visited[next_x][next_y][wall] == 0:
                    visited[next_x][next_y][wall] = visited[now_x][now_y][wall] + 1
                    deq.append([next_x, next_y, wall])
    
    return -1


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

print(bfs())