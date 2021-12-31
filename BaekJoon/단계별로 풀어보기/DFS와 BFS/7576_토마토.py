import sys
sys.stdin = open('7576_토마토.txt', 'rt')


from collections import deque


input = sys.stdin.readline
M, N = map(int, input().strip().split())
box = [list(map(int, input().strip().split())) for _ in range(N)]
red_tomato = [[i, j] for i in range(N) for j in range(M) if box[i][j] == 1]

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
def BFS(red_tomato):
    global box
    deq = deque(red_tomato)
    while deq:
        temp = deq.popleft()
        for d in dirs:
            test_x, test_y = temp[0]+d[0], temp[1]+d[1]
            if 0<=test_x<N and 0<=test_y<M and box[test_x][test_y] == 0:
                box[test_x][test_y] = box[temp[0]][temp[1]] + 1
                deq.append([test_x, test_y])


BFS(red_tomato)
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            sys.exit()

answer = 1
for i in range(N):
    answer = max(answer, max(box[i]))
print(answer-1)

