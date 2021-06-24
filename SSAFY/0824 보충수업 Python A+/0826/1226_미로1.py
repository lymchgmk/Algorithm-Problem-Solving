import sys
sys.stdin = open('1226_미로1.txt', 'r')

def Issafe(test, maze):
    N = len(maze)
    x, y = test[0], test[1]
    return (0 <= x < N and 0 <= y < N) and maze[x][y] != 1

def dfs(start, maze):
    visited=[]
    stack=[start]

    while stack:
        temp = stack.pop()
        x, y = temp[0], temp[1]
        if maze[x][y] == 3: return 1

        dir = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for i in range(4):
            test = [temp[0] + dir[i][0], temp[1] + dir[i][1]]
            
            if Issafe(test, maze) and test not in visited:
                visited.append(test)
                stack.append(test)

    return 0

for _ in range(10):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2: start = (i, j)
            if maze[i][j] == 3: end = (i, j)

    result = dfs(start, maze)
    print(f'#{test_case} {result}')