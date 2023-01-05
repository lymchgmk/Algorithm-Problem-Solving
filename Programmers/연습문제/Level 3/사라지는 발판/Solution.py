dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = 0, 0


def OOB(x, y):
    return x < 0 or x >= n or y < 0 or y >= m


vis = [[0] * 5 for _ in range(5)]
block = [[0] * 5 for _ in range(5)]


def solve(curx, cury, opx, opy):
    global vis, block

    if vis[curx][cury]: return 0

    ret = 0

    for dir in range(4):
        nx = curx + dx[dir]
        ny = cury + dy[dir]

        if OOB(nx, ny) or vis[nx][ny] or block[nx][ny] == 0: continue

        vis[curx][cury] = 1
        val = solve(opx, opy, nx, ny) + 1
        vis[curx][cury] = 0

        if ret % 2 == 0 and val % 2 == 1:
            ret = val
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val)
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val)

    return ret


def solution(board, aloc, bloc):
    global n, m

    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            block[i][j] = board[i][j]

    return solve(aloc[0], aloc[1], bloc[0], bloc[1])