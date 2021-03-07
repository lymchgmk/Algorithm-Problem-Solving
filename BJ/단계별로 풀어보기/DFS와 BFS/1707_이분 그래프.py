import sys
sys.stdin = open('1707_이분 그래프.txt', 'rt')
import collections


def bfs(v):
    global visited, color
    deq = collections.deque([v])
    visited[v] = True
    color[v] = True
    while deq:
        now = deq.popleft()
        for nxt in adj_lst[now]:
            if not visited[nxt]:
                deq.append(nxt)
                color[nxt] = not color[now]
                visited[nxt] = True
            else:
                if color[now] == color[nxt]:
                    return False
    return True


input = lambda: sys.stdin.readline().strip()
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    color = [False for _ in range(V+1)]
    flag = True
    for _ in range(E):
        a, b = map(int, input().split())
        adj_lst[a].append(b)
        adj_lst[b].append(a)
    
    for node in range(1, V+1):
        if not visited[node]:
            if not bfs(node):
                flag = False
                break
    
    print('YES' if flag else 'NO')
