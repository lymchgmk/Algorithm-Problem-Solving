import sys
sys.stdin = open('20061_모노미노도미노 2.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


N = int(input())

blue_board = [[0]*6 for _ in range(4)]
green_board = [[0]*4 for _ in range(6)]

total_point = 0
for _ in range(N):
    t, x, y = map(int, input().split())

    if t == 1:
        for i in range(6):
            if blue_board[x][i]:
                blue_board[x][i-1] = 1
                break
        else:
            blue_board[x][5] = 1
        
        green_board_col = [row[y] for row in green_board]
        for i in range(6):
            if green_board_col[i]:
                green_board[i-1][y] = 1
                break
        else:
            green_board[5][y] = 1

    elif t == 2:
        for i in range(6):
            if blue_board[x][i]:
                blue_board[x][i-1], blue_board[x][i-2] = 1, 1
                break
        else:
            blue_board[x][5], blue_board[x][4] = 1, 1
        
        green_board_col0 = [row[y] for row in green_board]
        green_board_col1 = [row[y+1] for row in green_board]
        for i in range(6):
            if green_board_col0[i] or green_board_col1[i]:
                green_board[i-1][y], green_board[i-1][y+1] = 1, 1
                break
        else:
            green_board[5][y], green_board[5][y+1] = 1, 1

    elif t == 3:
        for i in range(6):
            if blue_board[x][i] or blue_board[x+1][i]:
                blue_board[x][i-1], blue_board[x+1][i-1] = 1, 1
                break
        else:
            blue_board[x][5], blue_board[x+1][5] = 1, 1
        
        green_board_col = [row[y] for row in green_board]
        for i in range(6):
            if green_board_col[i]:
                green_board[i-1][y], green_board[i-2][y] = 1, 1
                break
        else:
            green_board[5][y], green_board[4][y] = 1, 1

    blue_point = 0
    while True:
        blue_temp_point = 0
        for i in range(5, -1, -1):
            blue_board_col = [row[i] for row in blue_board]
            if all(blue_board_col):
                blue_temp_point += 1
                for j in range(4):
                    blue_board[j] = [0] + blue_board[j][:i] + blue_board[j][i+1:]
                break

        blue_point += blue_temp_point
        if not blue_temp_point:
            break

    light_blue_board_col0 = [row[0] for row in blue_board]
    light_blue_board_col1 = [row[1] for row in blue_board]
    erase_blue_board_col = any(light_blue_board_col0) + any(light_blue_board_col1)
    if erase_blue_board_col:
        for i in range(4):
            blue_board[i] = [0]*erase_blue_board_col + blue_board[i][:-erase_blue_board_col]

    green_point = 0
    while True:
        green_temp_point = 0
        for i in range(5, -1, -1):
            green_board_row = green_board[i]
            if all(green_board_row):
                green_temp_point += 1
                green_board = [[0]*4] + green_board[:i] + green_board[i+1:]
                break

        green_point += green_temp_point
        if not green_temp_point:
            break

    light_green_board_row0 = green_board[0]
    light_green_board_row1 = green_board[1]
    erase_green_board_row = any(light_green_board_row0) + any(light_green_board_row1)
    if erase_green_board_row:
        green_board = [[0]*4]*erase_green_board_row + green_board[:-erase_green_board_row]

    total_point += blue_point
    total_point += green_point

total_tile = 0
for i in range(4):
    for j in range(6):
        total_tile += blue_board[i][j]
        total_tile += green_board[j][i]

print(total_point)
print(total_tile)