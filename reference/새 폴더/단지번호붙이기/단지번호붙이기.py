'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

def dfs(x, y):
    mat[x][y] = 0

    ret = 0
    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        xx, yy = x + dx, y + dy
        if not (0 <= xx < N and 0 <= yy < N): continue
        if mat[xx][yy]:
            ret += dfs(xx, yy)

    return ret + 1

N = int(input())
mat = [list(map(int, input())) for _ in range(N)]

res = []

for i in range(N):
    for j in range(N):
        if mat[i][j]:
            res.append(dfs(i, j))

res.sort()
print(len(res))
for i in res:
    print(i)
