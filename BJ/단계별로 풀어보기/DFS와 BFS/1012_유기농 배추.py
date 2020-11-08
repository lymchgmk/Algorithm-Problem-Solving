import sys
sys.stdin = open('1012_유기농 배추.txt', 'rt')


sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def DFS(x, y):
    global field
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    field[x][y] = -1
    for d in dirs:
        test_x, test_y = x + d[0], y + d[1]
        if 0<=test_x<N and 0<=test_y<M and field[test_x][test_y] == 1:
            field[test_x][test_y] = 0
            DFS(test_x, test_y)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    field = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        field[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                DFS(i, j)
                cnt += 1
    
    print(cnt)
    