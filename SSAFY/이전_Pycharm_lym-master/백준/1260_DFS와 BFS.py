import sys
import collections
sys.stdin = open("1260_DFS와 BFS.txt", "r")


def bfs(G, v):
    visited = [0 for _ in range(V + 1)]
    deq = collections.deque()

    deq.append(v)
    visited[v] = 1
    print(v, end=" ")
    while len(deq) != 0:
        v = deq.popleft()
        for w in range(1, V + 1):
            if G[v][w] == 1 and visited[w] == 0:
                deq.append(w)
                visited[w] = 1
                print(w, end=" ")

def dfs(G, v): # small v: 시작점
    visited[v] = 1
    print(v, end=" ")

    for w in range(V+1): # capital V: 총 정점 갯수
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


N, M, V = map(int, input().split()) # V가 정점
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(V + 1)]

for M_case in range(M):
    temp = list(map(int, input().split()))
    G[temp[0]][temp[1]] = 1
    G[temp[1]][temp[0]] = 1

dfs(G, V)
bfs(G, V)