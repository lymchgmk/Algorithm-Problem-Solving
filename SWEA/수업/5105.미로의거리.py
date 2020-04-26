import sys, collections
sys.stdin = open("5105.미로의거리.txt", "r")

def issafe(x, y):
    return (0 <= x < N and 0 <= y < N) and (maze[x][y] != 1)

def bfs(maze, start_x, start_y, end_x, end_y):

    visited[start_x][start_y]=1
    deq = collections.deque()
    deq.append([start_x, start_y])
    my_map[start_x][start_y] = 0

    while deq:
        temp = deq.popleft()

        if temp == [end_x, end_y]:
            return (my_map[end_x][end_y] - 1)

        for dir in range(4):
            test_x = temp[0] + dx[dir]
            test_y = temp[1] + dy[dir]

            if issafe(test_x, test_y):
                if visited[test_x][test_y] != 1:
                    my_map[test_x][test_y] = my_map[temp[0]][temp[1]] + 1
                    visited[test_x][test_y] = 1
                    deq.append([test_x, test_y])

    return 0


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j
            if maze[i][j] == 3:
                end_x, end_y = i, j

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    result = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    my_map = [[0 for _ in range(N)] for _ in range(N)]

    result = bfs(maze, start_x, start_y, end_x, end_y)
    print('#{} {}'.format(test_case, result))