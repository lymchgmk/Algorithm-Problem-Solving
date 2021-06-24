import sys
sys.stdin = open("4615_재미있는 오셀로 게임.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0]*N for _ in range(N)]
    #초기 돌 4개 놓을것
    board[int(N/2)][int(N/2)] = 2
    board[int(N/2) - 1][int(N/2)] = 1
    board[int(N/2) - 1][int(N/2) - 1] = 2
    board[int(N/2)][int(N/2) - 1] = 1

    for i in range(M):
        stone = list(map(int, input().split()))
        board[stone[1] - 1][stone[0] - 1] = stone[-1]

        for y in range(stone[1]-2, stone[1]+1):
            for x in range(stone[0]-2, stone[0]+1):