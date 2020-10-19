import sys
sys.stdin = open('1018_체스판 다시 칠하기.txt', 'rt')


N, M= map(int, input().split())
chess_board = [list(input()) for _ in range(N)]
result = N*M

for i in range(N-7):
    for j in range(M-7):
        start_color =  chess_board[i][j]
        count_1, count_2 = 0, 0
        for n in range(8):
            for m in range(8):
                if (n+m) % 2 == 0 and chess_board[i+n][j+m] != start_color:
                    count_1 += 1
                elif (n+m) % 2 == 1 and chess_board[i+n][j+m] == start_color:
                    count_1 += 1
                if (n+m) % 2 == 0 and chess_board[i+n][j+m] == start_color:
                    count_2 += 1
                elif (n+m) % 2 == 1 and chess_board[i+n][j+m] != start_color:
                    count_2 += 1
        count = min(count_1, count_2)
        if result > count:
            result = count
print(result)