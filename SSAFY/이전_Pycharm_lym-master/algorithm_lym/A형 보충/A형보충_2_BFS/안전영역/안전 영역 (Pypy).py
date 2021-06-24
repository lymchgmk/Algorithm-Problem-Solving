'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
5
'''
import collections

def BFS(x, y, k):
    deq = collections.deque();

    deq.append((x, y))
    visited[x][y] = 1

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N): continue
            if not visited[nx][ny] and mat[nx][ny] > k:
                deq.append((nx, ny))
                visited[nx][ny] = 1

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
ans = 1
dx = [-1, 1, 0,  0]
dy = [0, 0, -1, 1]
maxV = max(max(mat))
for k in range(1, maxV):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and mat[i][j] > k:
                BFS(i, j, k)
                cnt += 1
    ans = max(ans, cnt)

print(ans)