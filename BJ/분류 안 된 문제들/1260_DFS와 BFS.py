import sys
<<<<<<< HEAD
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
=======
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


N, M, V = map(int, input().split()) #정점의 개수, 간선의 개수, 시작 번호

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
>>>>>>> 79c8148ad04ab3814ac08b544d3eb4fac6bd6f68
