import sys
sys.stdin = open('1987_알파벳.txt', 'r')


def dfs(x, y, can_answer):
    global answer
    answer = max(answer, can_answer)
    
    for dir_x, dir_y in dirs:
        nx, ny = x+dir_x, y+dir_y
        if 0<=nx<R and 0<=ny<C and alphabet[board[nx][ny]] == 0:
            alphabet[board[nx][ny]] = 1
            dfs(nx, ny, can_answer+1)
            alphabet[board[nx][ny]] = 0
        

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)
R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)]
alphabet = [0]*26
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

answer = 1
alphabet[board[0][0]] = 1
dfs(0, 0, answer)

print(answer)
