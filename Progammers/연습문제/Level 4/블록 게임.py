from collections import defaultdict


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
    
    print(blocks)
    print(rectangles)

    return



if __name__ == "__main__":
    board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
    print(solution(board)) # 2