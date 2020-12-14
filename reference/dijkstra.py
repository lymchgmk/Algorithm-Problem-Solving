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