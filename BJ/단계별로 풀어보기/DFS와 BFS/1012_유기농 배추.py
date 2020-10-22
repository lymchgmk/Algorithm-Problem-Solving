import sys
sys.stdin = open('1012_유기농 배추.txt', 'rt')


def DFS(start):
    global visited
    visited.append(start)
    x, y = start
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for d in dirs:
        test_x, test_y = x+d[0], y+d[1]
        if 0<=test_x<M and 0<=test_y<N and field[test_x][test_y] == 1:
            test = [test_x, test_y]
            if test not in visited:
                DFS(test)



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1
    visited = []
    