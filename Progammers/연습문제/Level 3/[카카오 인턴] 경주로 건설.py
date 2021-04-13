from collections import deque


def solution(board):
    def bfs(start_x, start_y, start_dir):
        bfs_board = [[[board[y][x], None] for x in range(L)] for y in range(L)]
        bfs_board[0][0][1] = start_dir
        deq = deque([[start_x, start_y]])
        while deq:
            cur_x, cur_y = deq.popleft()
            cur_dir = bfs_board[cur_x][cur_y][1]
            for nxt_dir in dirs:
                nxt_x, nxt_y = cur_x + nxt_dir[0], cur_y + nxt_dir[1]
                if 0 <= nxt_x < L and 0 <= nxt_y < L and bfs_board[nxt_x][nxt_y][0] != 1:
                    if nxt_dir == cur_dir:
                        nxt_cost = bfs_board[cur_x][cur_y][0] + 100
                    else:
                        nxt_cost = bfs_board[cur_x][cur_y][0] + 600
                    
                    if bfs_board[nxt_x][nxt_y][0] == 0 or bfs_board[nxt_x][nxt_y][0] > nxt_cost:
                        bfs_board[nxt_x][nxt_y][0] = nxt_cost
                        bfs_board[nxt_x][nxt_y][1] = nxt_dir
                        deq.append([nxt_x, nxt_y])
        
        return bfs_board[-1][-1][0]

    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    L = len(board)
    
    # start_dir을 아래로 / 오른쪽으로 2가지 경우로 실행한 뒤, 최소값
    return min(bfs(0, 0, (1, 0)), bfs(0, 0, (0, 1)))



board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
