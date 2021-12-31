import sys
sys.stdin = open('2583_영역 구하기.txt', 'r')
import collections


def bfs(x, y):
    cnt = 1
    board[x][y] = 1
    q = collections.deque()
    q.append([x, y])
    while q:
        pop_x, pop_y = q.popleft()
        for dir_x, dir_y in dirs:
            new_x, new_y = pop_x+dir_x, pop_y+dir_y
            if 0<=new_x<M and 0<=new_y<N and board[new_x][new_y] == 0:
                board[new_x][new_y] = 1
                cnt += 1
                q.append([new_x, new_y])
    
    return cnt
    

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] += 1

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
result = []
for x in range(M):
    for y in range(N):
        if board[x][y] == 0:
            result.append(bfs(x, y))

print(len(result))
print(*sorted(result))

