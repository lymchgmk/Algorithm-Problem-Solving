from collections import deque
from copy import deepcopy

def solution(board):
    def horizontal_or_vertical(p1, p2):
        if p1[0] - p2[0]:
            return 'vertical'
        else:
            return 'horizontal'
    
    def bfs(left_wing, right_wing):
        # 현 위치
        # 움직일 수 있는 모든 위치
        # board에 2 입력
        # 위치 교환
        cnt = 0
        cur_deq = deque([left_wing, right_wing])
        while board[-1][-1] != 2:
            nxt_deq = deque()
            while cur_deq:
                cur_left_wing, cur_right_wing = cur_deq.popleft()
                if horizontal_or_vertical(cur_left_wing, cur_right_wing):
                    pass
                else:
                    pass
            
    
    bfs([0, 0], [0, 1])
    return
    
    


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

for b in board:
    print(b)
    
print(solution(board))
