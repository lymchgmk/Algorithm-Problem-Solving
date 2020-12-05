import sys
sys.stdin = open("1520_내리막 길.txt", "rt")
input = lambda: sys.stdin.readline().strip()


sys.setrecursionlimit(3000)


def DFS(start):
    x, y = start

    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for d in dirs:
        nx, ny = x + d[0], y + d[1]
        if 0<=nx<M and 0<=ny<N and MAP[nx][ny] < MAP[x][y]:
            dp[x][y] += DFS([nx, ny])
    
    return dp[x][y]


M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
dirs = [[1,0], [-1,0], [0,1], [0,-1]]
print(DFS([0, 0]))