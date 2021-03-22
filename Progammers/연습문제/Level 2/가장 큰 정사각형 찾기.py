def solution(board):
    def find_n_square(p, n):
        for i in range(p[0], p[0]+n):
            for j in range(p[1], p[1]+n):
                if 0<=i<len(board) and 0<=j<len(board):
                    if not board[i][j]:
                        return False
        return True
    
    for n in range(len(board), 0, -1):
        for i in range(len(board)):
            for j in range(len(board)):
                if find_n_square([i, j], n):
                    return n*n
                


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))