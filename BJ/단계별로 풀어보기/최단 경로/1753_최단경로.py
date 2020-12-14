import sys
sys.stdin = open("1753_최단경로.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


# 단일-출발 최단 경로 문제
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
    now_dist, now_idx = heapq.heappop(heap_queue)
    for next in adj[now_idx]:
        next_idx, next_dist = next
        if dist[next_idx] > now_dist + next_dist:
            dist[next_idx] = now_dist + next_dist
            heapq.heappush(heap_queue, [dist[next_idx], next_idx])

answer = [dist[i] if dist[i] != INF else "INF" for i in range(1, V+1)]
print(*answer)