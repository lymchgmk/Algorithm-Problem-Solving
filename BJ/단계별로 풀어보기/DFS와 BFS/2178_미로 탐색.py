import sys
sys.stdin = open('2178_미로 탐색.txt', 'rt')


from collections import deque


def BFS(start):
    global BFS_visited

    deq = deque()
    deq.append(start)
    BFS_visited.append(start)
    
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while deq:
        test = deq.popleft()
        if test == [N-1, M-1]:
            break
        for d in dirs:
            x, y = test[0]+d[0], test[1]+d[1]
            if 0<=x<N and 0<=y<M and maze[x][y] == 1 and [x,y] not in BFS_visited:
                BFS_visited.append([x, y])
                deq.append([x, y])


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
BFS_visited = []
BFS([0, 0])
print(len(BFS_visited))