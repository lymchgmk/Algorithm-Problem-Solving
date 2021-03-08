import sys
sys.stdin = open('4963_섬의 개수.txt', 'r')


def dfs(x, y):
    board[x][y] = 0
    for dir in dirs:
        nx, ny = x+dir[0], y+dir[1]
        if 0<=nx<h and 0<=ny<w and board[nx][ny] == 1:
            dfs(nx, ny)


input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(h)]
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    count = 0
    for x in range(h):
        for y in range(w):
            if board[x][y] == 1:
                dfs(x, y)
                count += 1
    
    print(count)
