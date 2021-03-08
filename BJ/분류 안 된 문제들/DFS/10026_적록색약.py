import sys
sys.stdin = open('10026_적록색약.txt', 'r')
import copy


def dfs(y, x):
    stack = []
    stack.append([y, x, board[y][x]])
    board[y][x] = 'X'
    while stack:
        pop_y, pop_x, color = stack.pop()
        for dir_y, dir_x in dirs:
            new_y, new_x = pop_y+dir_y, pop_x+dir_x
            if 0<=new_y<N and 0<=new_x<N and board[new_y][new_x] != 'X' and board[new_y][new_x] == color:
                stack.append([new_y, new_x, board[new_y][new_x]])
                board[new_y][new_x] = 'X'
                
    return 1
    

def dfs_R_is_G(y, x):
    stack = []
    stack.append([y, x, board_R_is_G[y][x]])
    while stack:
        pop_y, pop_x, color = stack.pop()
        for dir_y, dir_x in dirs:
            new_y, new_x = pop_y+dir_y, pop_x+dir_x
            if 0<=new_y<N and 0<=new_x<N and board_R_is_G[new_y][new_x] != 'X':
                if (board_R_is_G[new_y][new_x] == color) or (board_R_is_G[new_y][new_x] in ['R', 'G'] and color in ['R', 'G']):
                    stack.append([new_y, new_x, board_R_is_G[new_y][new_x]])
                    board_R_is_G[new_y][new_x] = 'X'
                    
    return 1


input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)

N = int(input())
board = [list(input()) for _ in range(N)]
board_R_is_G = copy.deepcopy(board)
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

result = []
cnt = 0
for y in range(N):
    for x in range(N):
        if board[y][x] != 'X':
            cnt += dfs(y, x)
result.append(cnt)

cnt_R_is_G = 0
for y in range(N):
    for x in range(N):
        if board_R_is_G[y][x] != 'X':
            cnt_R_is_G += dfs_R_is_G(y, x)
result.append(cnt_R_is_G)

print(*result)
