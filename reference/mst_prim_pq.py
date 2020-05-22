V, E = map(int, input().split())
adj = [[0]*V for _ in range(V)]

for i in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])
# print(adj)

# key, mst, 우선순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []

# 시작 정점 선택 : 0
key[0] = 0
# 큐에 시작 정점을 넣음 -> (key, 정점 인덱스)
# 우선 순위 큐 -> 이진 힙 -> headpq 라이브러리 사용
heapq.heappush(pq, (0, 0))

while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    # mst로 선택
    mst[node] = True
    result += k
    # key 갱신 => key 배열/ 큐
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는
            heapq.heappush(pq, (key[dest], dest))

print(result)