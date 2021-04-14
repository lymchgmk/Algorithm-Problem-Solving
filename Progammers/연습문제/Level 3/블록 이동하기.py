from collections import deque
from copy import deepcopy

def solution(board):
    def bfs(left_wing, right_wing):
        deq = deque([[left_wing, right_wing]])
        while deq:
            cur_left_wing, cur_right_wing = deq.popleft()
            # 현재 상태 가로인지 세로인지 체크
            # 가로
            if cur_left_wing[0] - cur_right_wing[0]:
                if cur_right_wing + 1 < len(board) and board[cur_right_wing[0]][cur_right_wing + 1]
            # 세로
            else:
                pass
    
    bfs([0, 0], [0, 1])
    return
    
    


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# 로봇 현재 위치를 2로 표시
board[0][0], board[0][1] = 2, 2

# 평행이동하는 경우 / 회전하는 경우



for b in board:
    print(b)
print(solution(board))
