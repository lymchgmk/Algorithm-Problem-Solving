import sys
sys.stdin = open("BJ_13460_구슬 탈출 2.txt")

# def move():
#     LT, RT, UP, DW

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            RED = (i, j)
        elif board[i][j] == "B":
            BLUE = (i, j)
        elif board[i][j] == "O":
            HOLE = (i, j)



