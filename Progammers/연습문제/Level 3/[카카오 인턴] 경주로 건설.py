from collections import deque


def solution(board):
    def bfs(start_x, start_y, start_dir):
        bfs_board = [[[board[y][x], None] for x in range(L)] for y in range(L)]
        bfs_board[0][0][1] = start_dir
        
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
    
    # start_dir을 아래로 / 오른쪽으로 2가지 경우로 실행한 뒤, 최소값
    return min(bfs(0, 0, (1, 0)), bfs(0, 0, (0, 1)))



board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
