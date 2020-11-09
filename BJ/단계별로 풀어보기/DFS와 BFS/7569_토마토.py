import sys
sys.stdin = open('7569_토마토.txt', 'rt')


from collections import deque


input = sys.stdin.readline
M, N, H = map(int, input().strip().split())
box = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]
red_tomato = [[k, i, j] for k in range(H) for i in range(N) for j in range(M) if box[k][i][j] == 1]

dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
def BFS(red_tomato):
    global box
    deq = deque(red_tomato)
    while deq:
        temp = deq.popleft()
        for d in dirs:
            test_z, test_x, test_y = temp[0]+d[0], temp[1]+d[1], temp[2]+d[2]
            if 0<=test_z<H and 0<=test_x<N and 0<=test_y<M and box[test_z][test_x][test_y] == 0:
                box[test_z][test_x][test_y] = box[temp[0]][temp[1]][temp[2]] + 1
                deq.append([test_z, test_x, test_y])


BFS(red_tomato)
for i in range(N):
    for j in range(M):
        for k in range(H):
            if box[k][i][j] == 0:
                print(-1)
                sys.exit()

answer = 1
for k in range(H):
    for i in range(N):
        answer = max(answer, max(box[k][i]))
print(answer-1)  

