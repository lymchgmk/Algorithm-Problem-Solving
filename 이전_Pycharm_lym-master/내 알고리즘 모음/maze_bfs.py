import sys
import collections

sys.stdin = open("test.txt", "r")

def issafe(x, y):
    return (0 <= x < N and 0 <= y < M) and maze[x][y] == 1

def bfs(maze, start_x, start_y):

    visited.append([start_x, start_y])
    deq = collections.deque()
    deq.append([start_x, start_y])
    count = 0
    my_map[start_x][start_y] = count

    while deq:
        temp = deq.popleft()
        if temp[0] == N-1 and temp[1] == M-1:
            return my_map[N-1][M-1]

        count += 1

        for dir in range(4):
            test_x = temp[0] + dx[dir]
            test_y = temp[1] + dy[dir]

            if issafe(test_x, test_y):
                if maze[test_x][test_y] == 1 and [test_x, test_y] not in visited:
                    visited.append([test_x, test_y])
                    deq.append([test_x, test_y])
                    my_map[test_x][test_y] = count



N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 기본 세팅

start_x, start_y = 0, 0

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

result = 0
visited = []
my_map = [[0 for _ in range(M)] for _ in range(N)]

print(bfs(maze, start_x, start_y))
print(my_map)