from collections import deque
from copy import deepcopy

def solution(board):
    def bfs(left_wing, right_wing):
        cnt = 0
        deq = deque([left_wing, right_wing])
        while True:
            tmp = deque()
            
            if board[-1][-1] == 2:
                return cnt
            
            if not deq:
                deq, tmp = tmp, deque()
    
    bfs([0, 0], [0, 1])
    return
    
    


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# 로봇 현재 위치를 2로 표시
board[0][0], board[0][1] = 2, 2

# 평행이동하는 경우 / 회전하는 경우



for b in board:
    print(b)
print(solution(board))
