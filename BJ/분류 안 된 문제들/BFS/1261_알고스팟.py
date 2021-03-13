import sys
sys.stdin = open('1261_알고스팟.txt', 'rt')
import collections


input = lambda: sys.stdin.readline().strip()
M, N = map(int, input().split())
MAZE = [list(map(int, input())) for _ in range(N)]

dist = [[-1]*M for _ in range(N)]
dist[0][0] = 0
deq = collections.deque([[0, 0]])
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
while deq:
    x, y = deq.popleft()
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and dist[nx][ny] == -1:
            if MAZE[nx][ny] == 0:
                deq.appendleft([nx, ny])
                dist[nx][ny] = dist[x][y]
            elif MAZE[nx][ny] == 1:
                deq.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1

print(dist[N-1][M-1])
