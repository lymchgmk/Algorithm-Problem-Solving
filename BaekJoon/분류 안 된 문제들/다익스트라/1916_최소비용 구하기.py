import sys
sys.stdin = open('1916_최소비용 구하기.txt', 'rt')
import collections
import heapq


input = lambda: sys.stdin.readline().strip()
N = int(input())
M = int(input())
adj = collections.defaultdict(list)
for _ in range(M):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])
start, end = map(int, input().split())

INF = float('inf')
dist = [INF]*(N+1)
selected = [False]*(N+1)

dist[start] = 0
cnt = 0
while cnt < N:
    temp_min = INF
    u = -1
    for i in range(1, N+1):
        if not selected[i] and dist[i] < temp_min:
            temp_min = dist[i]
            u = i
    # 결정
    selected[u] = True
    cnt += 1
    # 간선완화
    for w, cost in adj[u]:
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
            
print(dist[end])


'''
V, E = map(int, input().split())
adj = {i:[] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])

INF = float('inf')
dist = [INF]*V
selected = [False]*V

dist[0] = 0
cnt = 0
while cnt < V:
    #dist가 최소인 정점 찾기
    min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < min:
            min = dist[i]
            u = i
    #결정
    selected[u] = True
    cnt += 1
    #간선완화
    for w, cost in adj[u]:
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
print(dist)'''