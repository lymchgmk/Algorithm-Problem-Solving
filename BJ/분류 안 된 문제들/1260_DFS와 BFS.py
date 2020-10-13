import sys
sys.stdin = open('1260_DFS와 BFS.txt', 'r')
from collections import deque


def bfs(start):
    global bfs_visited, bfs_result
    deq = deque()
    deq.append(start)
    bfs_visited.append(start)

    while deq:
        now = deq.popleft()
        bfs_result.append(now)
        for next in adj_matrix[now]:
            if next not in bfs_visited:
                bfs_visited.append(next)
                deq.append(next)
                

def dfs(node):
    global dfs_visited
    dfs_visited.append(node)

    for next in adj_matrix[node]:
        if next not in dfs_visited:
            dfs(next)


N, M, V = map(int, input().split())

adj_matrix = [list() for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_matrix[x].append(y)
    adj_matrix[y].append(x)
for x in adj_matrix:
    x.sort()

dfs_visited = []
bfs_visited, bfs_result = [], []

dfs(V)
bfs(V)

print(*dfs_visited)
print(*bfs_result)
