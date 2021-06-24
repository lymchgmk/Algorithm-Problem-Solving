def check(sx, sy, dol):
    for i in range(8):
        x = sx   # sx와 sy를 시작점으로 기억해야 함.
        y = sy
        flag = False

        while x + dx[i] > 0 and x + dx[i] <= N and y + dy[i] > 0 and y + dy[i] <= N : # 벽이 아니면 주어진 방향으로 계속 증가
            x += dx[i]
            y += dy[i]
            if pan[x][y] == 0: break    # 0 이면  break
            if pan[x][y] == dol:        # 같은 돌이면 flag체크하고 endX, endY 변경
                flag = True
                ex = x  #end x
                ey = y  #end y
                break                   # 가까운 위치의 같은 색상의 돌을 찾고 그만해야 함.
        if flag:  # flag가 1 이면 (x,y) ~ (ex, ey)까지 dol변수의 값으로 변경
            x = sx
            y = sy
            while not(x == ex and y == ey):
                x += dx[i]
                y += dy[i]
                pan[x][y] = dol

def printArr():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(pan[i][j], end=" ")
        print()
    print()

import sys
sys.stdin = open("(4615)재미있는오셀로게임_input.txt")
dx = [-1, -1, -1, 0, 1, 1,  1,  0]
dy = [-1,  0,  1, 1, 1, 0, -1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pan = [[0 for _ in range(N+1)] for _ in range(N+1)]   #인덱스를 1부터 사용

    mid = N // 2
    # W = 2, B = 1  초기화
    pan[mid][mid] = pan[mid+1][mid+1] = 2
    pan[mid][mid+1] = pan[mid+1][mid] = 1
    #printArr()

    for i in range(M):  # 좌표는 1부터 시작함.
        a, b, dol = map(int, input().split())
        pan[a][b] = dol
        check(a, b, dol)
        # printArr()

    B = 0
    W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if pan[i][j] == 1 : B += 1
            if pan[i][j] == 2 : W += 1

    print("#{} {} {}".format(tc, B, W))