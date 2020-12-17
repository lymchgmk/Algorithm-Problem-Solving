import sys
sys.stdin = open("1504_특정한 최단 경로.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


def dijkstra(s, e):
    dist = [INF]*N
    dist[s] = 0

    hq = []
    heapq.heappush(hq, [0, s])
    while hq:
        now_w, now_x = heapq.heappop(hq)
        for next_w, next_x in adj[now_x]:
            next_w += now_w
            if next_w < dist[next_x]:
                dist[next_x] = next_w
                heapq.heappush(hq, [next_w, next_x])

    return dist[e]


N, E = map(int, input().split())
adj = {i:[] for i in range(N)}
for _ in range(E):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append([c, b])
    adj[b].append([c, a])

v1, v2 = map(lambda x: int(x) - 1, input().split())
INF = float('inf')

answer1 = dijkstra(0, v1) + dijkstra(v1, v2) + dijkstra(v2, N-1)
answer2 = dijkstra(0, v2) + dijkstra(v2, v1) + dijkstra(v1, N-1)
answer = min(answer1, answer2)
if answer == INF:
    answer = -1
print(answer)