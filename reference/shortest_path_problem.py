# 1. 단일-출발 최단 경로 문제
# 2. 단일-도착 최단 경로 문제
# 3. 전체-쌍 최단 경로 문제

# 데이크스트라 알고리즘 : 단일-쌍, 단일-출발, 단일-도착
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
print(dist)


# heapq 사용해서 속도 향상한 경우
'''
V, E = map(int, input().split())
K = int(input())
adj = {i: [] for i in range(V+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

INF = float('inf')
dist = [INF]*(V+1)
dist[K] = 0

heap_queue = []
heapq.heappush(heap_queue, [0, K])
while heap_queue:
    node = heapq.heappop(heap_queue)
    for end in adj[node[1]]:
        if dist[end[0]] > node[0] + end[1]:
            dist[end[0]] = node[0] + end[1]
            heapq.heappush(heap_queue, [dist[end[0]], end[0]])

answer = [dist[i] if dist[i] != INF else "INF" for i in range(1, V+1)]
print(*answer)
'''


# 벨먼-포드 알고리즘 : 가중치가 음수라면 단일-출발
def bellman_ford():
    global isUpdated

    for repeat in range(N):
        for i in range(1, N+1):
            for b, c in adj[i]:
                if dist[i] != INF and dist[b] > dist[i] + c:
                    dist[b] = dist[i] + c
                    if repeat == N-1:
                        isUpdated = False
    
    return


N, M = map(int, input().split())
INF = float('inf')
dist = [INF]*(N+1)
dist[1] = 0
isUpdated = True

adj = {i:[] for i in range(N+1)}
for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append([B, C])

bellman_ford()

# A* 탐색 알고리즘 : 탐색 속도 향상을 위한 휴리스틱 방법, 단일-쌍

# 플로이드-와셜 알고리즘 : 전체-쌍
def floyd_warshall():
    global dist

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j != k and dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]
    
    return dist


n = int(input())
m = int(input())
INF = float('inf')
dist = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(lambda x: int(x)-1, input().split())
    c += 1
    dist[a][b] = min(dist[a][b], c)

ans = floyd_warshall()
for i in range(n):
    for j in range(n):
        if ans[i][j] == INF:
            ans[i][j] = 0
    print(*ans[i])