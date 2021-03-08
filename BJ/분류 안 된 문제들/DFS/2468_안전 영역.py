import sys
sys.stdin = open('2468_안전 영역.txt', 'r')
import copy


def dfs(x, y):
    tmp_field[x][y] = 0
    for dir in dirs:
        nx, ny = x+dir[0], y+dir[1]
        if 0<=nx<N and 0<=ny<N and tmp_field[nx][ny] > rain:
            dfs(nx, ny)

sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().strip()
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
result = 0
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
for rain in range(0, 101):
    cnt = 0
    tmp_field = copy.deepcopy(field)
    for x in range(N):
        for y in range(N):
            if tmp_field[x][y] > rain:
                dfs(x, y)
                cnt += 1

    result = max(result, cnt)
    if cnt == 0:
        break

print(result)
