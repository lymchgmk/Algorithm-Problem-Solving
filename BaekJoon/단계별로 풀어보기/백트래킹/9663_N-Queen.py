import sys
sys.stdin = open("9663_N-Queen.txt", "rt")


def chk(row, col):
    if chk_col[col] == 1 or chk_dgn_fwd[row+col] == 1 or chk_dgn_rev[row - col + N-1] == 1:
        return False
    else:
        return True

    
def dfs(row):
    if row == N:
        return 1
    
    result = 0
    for col in range(N):
        if chk(row, col):
            chess_board[row][col] = 1
            chk_col[col], chk_dgn_fwd[row + col], chk_dgn_rev[row - col + N-1] = 1, 1, 1
            result += dfs(row + 1)
            chess_board[row][col] = 0
            chk_col[col], chk_dgn_fwd[row + col], chk_dgn_rev[row - col + N-1] = 0, 0, 0
    return result


N = int(input())
chess_board = [[0]* N for _ in range(N)]
chk_col = [0] * N
chk_dgn_fwd, chk_dgn_rev = [0] * (2*N-1), [0] * (2*N-1)
print(dfs(0))