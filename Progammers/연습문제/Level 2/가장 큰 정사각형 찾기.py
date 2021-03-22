def solution(board):
    L_x, L_y = len(board), len(board[0])
    _max = max(max(board))
    for i in range(1, L_x):
        for j in range(1, L_y):
            if board[i][j]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                _max = max(_max, board[i][j])
    return _max**2


board = [[1,0],[0,0]]
print(solution(board))