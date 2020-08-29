def dfs(x, y, group):
    visited[x][y] = 1;
    mat[x][y] = group;
    count[group] += 1;

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < N): continue
        if visited[nx][ny]: continue
        if mat[nx][ny] == 0 : continue
        dfs(nx, ny, group)

import sys
sys.stdin = open("단지번호붙이기_input.txt")
N = int(input())
mat = [list(map(int, input())) for _ in range(N)] # 단지 입력 받음
visited = [[0 for _ in range(N)] for _ in range(N)] # 방문이력 들어갈 NxN 리스트 만들기
group = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = [0] * (N*N+1) # +1 한 이유는 인덱스 0을 비워두고 사용하려고?

for i in range(N):
    for j in range(N):
        if mat[i][j] and visited[i][j] == 0: # mat !=0 and visited == 0 인 경우
            dfs(i, j, group)
            group += 1

count.sort()
print(group-1)
for i in count:
    if i != 0:
        print(i)
