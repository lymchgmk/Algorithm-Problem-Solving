import sys
sys.stdin = open('2580_스도쿠.txt', 'r')

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def check_numbers(position):
    result = list(range(10))

    row = sudoku_board[position[0]]
    for r in row:
        if r in result:
            result.remove(r)

    col = [sudoku_board[c][position[1]] for c in range(9)]
    for c in col:
        if c in result:
            result.remove(c)

    sqr = [(position[0] // 3) * 3, (position[1] // 3) * 3]
    for i in range(3):
        for j in range(3):
            s = sudoku_board[sqr[0] + i][sqr[1] + j]
            if s in result:
                result.remove(s)

    return result


def sudoku(n):
    if len(zero_position) == n:
        for i in range(9):
            print(*sudoku_board[i])
        sys.exit()

    else:
        for num in check_numbers(zero_position[n]):
            sudoku_board[zero_position[n][0]][zero_position[n][1]] = num
            sudoku(n + 1)
            sudoku_board[zero_position[n][0]][zero_position[n][1]] = 0


sudoku_board = [list(map(int, input().strip().split())) for _ in range(9)]
zero_position = [[i, j] for i in range(9) for j in range(9) if sudoku_board[i][j] == 0]
sudoku(0)