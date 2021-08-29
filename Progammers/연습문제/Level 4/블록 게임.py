from collections import defaultdict


def _check(key, black_blocks, board) :
    for x, y in black_blocks[key]:
        print(key, x, y)
        for i in range(len(board)-y):
            if board[i][y] != 0:
                return False
    return True


def _remove(key, blocks, board):
    for x, y in blocks[key]:
        board[x][y] = 0
    return board
    
    
def solution(board):
    N = len(board)
    blocks = defaultdict(set)
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                blocks[board[i][j]].add((i, j))
                
    rectangles = defaultdict(set)
    for key, block in blocks.items():
        x_list, y_list = zip(*block)
        x_min, x_max = min(x_list), max(x_list)
        y_min, y_max = min(y_list), max(y_list)
        rectangles[key].update([(x, y) for x in range(x_min, x_max+1) for y in range(y_min, y_max+1)])
    
    black_blocks = defaultdict(set)
    for key in blocks.keys():
        black_blocks[key].update(rectangles[key] - blocks[key])

    answer = 0
    _answer = 0
    for key in blocks.keys():
        if _check(key, black_blocks, board):
            print(key, _check(key, black_blocks, board))


    return


if __name__ == "__main__":
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
    print(solution(board)) # 2