import sys
sys.stdin = open('11724_연결 요소의 개수.txt', 'r')


def dfs(now):
    visited[now] = True
    for nxt in adj[now]:
        if not visited[nxt]:
            dfs(nxt)


input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())

visited = [False]*(N+1)
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
