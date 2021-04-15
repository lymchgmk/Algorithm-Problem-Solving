from collections import deque
from copy import deepcopy

def solution(board):
    def horizontal_or_vertical(p1, p2):
        return p1[0] == p2[0]
    
    def bfs(left_wing, right_wing):
        L = len(board)
        cnt = 0
        cur_deq, nxt_deq = deque([left_wing, right_wing]), deque()
        while board[-1][-1] != 2:
            while cur_deq:
                cur_left_wing, cur_right_wing = sorted(cur_deq.popleft())
                # horizontal
                if horizontal_or_vertical(cur_left_wing, cur_right_wing):
                    left_x, left_y = cur_left_wing
                    right_x, right_y = cur_right_wing
                    # 수평
                    if 0 <= left_y - 1: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    if right_y + 1 < L: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    # 수직
                    if 0 <= left_x - 1: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    if right_x + 1 < L: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    # 회전
                    for i in range(2):
                        for j in range(2):
                            if 0<=left_x+i<L and 0<=left_y+j<L:
                                if board[left_x+i][left_y+j] == 1:
                                    can_rotate = False
                                    break
                    else:
                        can_rotate = True
                    
                    if can_rotate:
                        nxt_deq.append([[left_x, left_y], [left_x + 1, left_y]])
                        nxt_deq.append([[left_x, left_y + 1], [left_x + 1, left_y + 1]])
                    
                        
                else:
                    left_x, left_y = cur_left_wing
                    right_x, right_y = cur_right_wing
                    # 수평
                    if 0 <= left_y - 1: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    if right_y + 1 < L: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    # 수직
                    if 0 <= left_x - 1: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    if right_x + 1 < L: nxt_deq.append([[left_x - 1, left_y], [right_x - 1, right_y]])
                    # 회전
                    for i in range(2):
                        for j in range(2):
                            if 0 <= left_x + i < L and 0 <= left_y + j < L:
                                if board[left_x + i][left_y + j] == 1:
                                    can_rotate = False
                                    break
                    else:
                        can_rotate = True
    
                    if can_rotate:
                        nxt_deq.append([[left_x, left_y], [left_x + 1, left_y]])
                        nxt_deq.append([[left_x, left_y + 1], [left_x + 1, left_y + 1]])
                
            for nxt_left_wing, nxt_right_wing in nxt_deq:
                board[nxt_left_wing[0]][nxt_left_wing[1]] = 2
                board[nxt_right_wing][0][nxt_right_wing[1]] = 2
                
            cur_deq, nxt_deq = nxt_deq, deque()
            
            cnt += 1

        return cnt

    return bfs([0, 0], [0, 1])
    
    


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

for b in board:
    print(b)
    
print(solution(board))
