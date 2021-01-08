import sys
import heapq
sys.stdin = open('(5249)최소신장트리_input.txt', 'r')
T = int(input())
INF = float('inf')

def mst():
    pq = []
    total = 0
    u = 0  # 시작점을 0으로
    D[u] = 0
    heapq.heappush(pq, (D[u], u))

    while pq:
        # 가중치 최소값 찾기
        d, u = heapq.heappop(pq)
        if visited[u]:continue

        # 방문처리, 계산
        visited[u] = 1
        total += d

        # 인접한 정점 갱신
        for v, d in adj[u]:
            if visited[v] == 0 and d < D[v]:
                D[v] = d
                PI[v] = d
                heapq.heappush(pq, (D[v], v))

    return total


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    D = [INF] * (V + 1)
    PI = list(range(V + 1))
    visited = [0] * (V + 1)
    adj = {i: [] for i in range(V+1)}
    for i in range(E):   # 인접리스트
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        adj[e].append([s, c])
    print('#{} {}'.format(tc, mst()))