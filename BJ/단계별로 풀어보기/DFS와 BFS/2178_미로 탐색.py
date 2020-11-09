import sys
sys.stdin = open('2178_미로 탐색.txt', 'rt')


from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))


def BFS(x, y):
    deq = deque([[x, y]])
    while deq:
        temp = deq.popleft()
        for i in range(4):
            test_x, test_y = temp[0] + dirs[i][0], temp[1] + dirs[i][1]
            if 0<=test_x<N and 0<=test_y<M and maze[test_x][test_y] == 1:
                maze[test_x][test_y] = maze[temp[0]][temp[1]] + 1
                deq.append([test_x, test_y])


BFS(0, 0)
print(maze[N-1][M-1])