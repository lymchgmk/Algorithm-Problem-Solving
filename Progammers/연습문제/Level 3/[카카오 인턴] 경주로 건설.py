from collections import deque


def solution(board):
    def bfs(start_x, start_y, start_dir):
        deq = deque([[start_x, start_y, start_dir]])
        while deq:
            cur_x, cur_y, cur_dir = deq.popleft()
            for nxt_dir in dirs:
                nxt_x, nxt_y = cur_x + nxt_dir[0], cur_y + nxt_dir[1]
                if 0 <= nxt_x < L and 0 <= nxt_y < L and not cost_board[nxt_x][nxt_y][0]:
                    if cur_dir == 'start_dir' or cur_dir == nxt_dir:
                        nxt_cost = cost_board[cur_x][cur_y][1] + 100
                    elif cur_dir != nxt_dir:
                        nxt_cost = cost_board[cur_x][cur_y][1] + 600
                    
                    if cost_board[nxt_x][nxt_y][2] != 'start_dir' and not cost_board[nxt_x][nxt_y][1] or cost_board[nxt_x][nxt_y][1] > nxt_cost:
                        cost_board[nxt_x][nxt_y][1] = nxt_cost
                        cost_board[nxt_x][nxt_y][2] = nxt_dir
                        deq.append([nxt_x, nxt_y, nxt_dir])
                        

    
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    L = len(board)
    # 벽 유무, cost, dir
    cost_board = [[[board[y][x], 0, None] for x in range(L)] for y in range(L)]
    cost_board[0][0][2] = 'start_dir'
    
    # start_dir을 아래로 / 오른쪽으로 2가지 경우로 실행한 뒤, 최소값
    bfs(0, 0, 'start_dir')
    
    for c in cost_board:
        print(list(tmp[1] for tmp in c))
    
    return cost_board[L-1][L-1][1]


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
