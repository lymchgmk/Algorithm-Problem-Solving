import sys
sys.stdin = open("미로.txt", "r")

def Issafe(x, y): # 범위 안의 좌표인지 and (maze 벽에 안닿았음 or 시작점 다시 지나도 괜찮)
    return (0<= x < N and 0 <= y < N) and (maze[x][y] == 0 or maze[x][y] == 3)

def dfs(start_x, start_y):
    global result # 나중에 result 리턴할 것이기 때문

    if maze[start_x][start_y] == 3:
        result = 1
        return

    visited.append((start_x, start_y))

    for dir in range(4):
        test_x = start_x + dx[dir]
        test_y = start_y + dy[dir]
        if Issafe(test_x, test_y) and ((test_x, test_y) not in visited): # 탐색해도 되는 좌표 and 안 가본 좌표
            dfs(test_x, test_y) # 재귀해서 다시 탐색

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    #print(maze)

    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                start_x, start_y = x, y # 시작점 찾음

    dx = [0, 0, 1, -1] # 2차원에서 움직일 경우
    dy = [1, -1, 0, 0]

    visited = []
    result = 0
    dfs(start_x, start_y) # dfs 함수 적용 -- 재귀하면서 모든 곳에 가볼 것
    print("#{} {}".format(test_case, result))