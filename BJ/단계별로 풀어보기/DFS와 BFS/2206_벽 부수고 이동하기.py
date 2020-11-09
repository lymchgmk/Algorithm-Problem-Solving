import sys
sys.stdin = open('2206_벽 부수고 이동하기.txt', 'rt')


from collections import deque


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dist = [[[0, 0] for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 1
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def BFS():
    global dist
    deq = deque([(0, 0, 0)])
    while deq:
        x, y, w = deq.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y][w]
        
        for d in dirs:
            test_x, test_y = x + d[0], y + d[1]
            if test_x < 0 or test_x >= N or test_y < 0 or test_y >= M:
                continue
            if dist[test_x][test_y][w]:
                continue
            if arr[test_x][test_y] == '0':
                dist[test_x][test_y][w] = dist[test_x][test_y][w] + 1
                deq.append((test_x, test_y, w))
            if arr[test_x][test_y] == '1' and w == 0:
                dist[test_x][test_y][1] = dist[test_x][test_y][w] + 1
                deq.append((test_x, test_y, 1))
    return -1

print(BFS())