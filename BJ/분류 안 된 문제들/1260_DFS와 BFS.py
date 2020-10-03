import sys
from collections import deque
sys.stdin=open("1260_DFS와 BFS.txt")


def dfs(start):
    global dfs_visited
    stack = [start]

    while stack:
        temp = stack.pop()
        for i in range(N+1):
            if adj_matrix[temp][i] == 1 and i not in dfs_visited:
                dfs(i)

    return dfs_visited


def bfs(start):
    deq = deque()
    deq.append(start)
    visited = [start]

    while deq:
        temp = deq.popleft()
        for i in range(1, N+1):
            if adj_matrix[temp][i] == 1 and i not in visited:
                deq.append(i)
                visited.append(i)

    return visited



N, M, V = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
adj_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for d in data:
    adj_matrix[d[0]][d[1]] = 1
    adj_matrix[d[1]][d[0]] = 1

dfs_visited = []

print(dfs(V))
print(bfs(V))