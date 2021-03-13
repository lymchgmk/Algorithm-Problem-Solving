import sys
sys.stdin = open('1238_파티.txt', 'rt')
import collections
import heapq


def dijkstra(start):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    heap_queue = []
    heapq.heappush(heap_queue, [0, start])
    while heap_queue:
        node = heapq.heappop(heap_queue)
        for end in adj[node[1]]:
            if dist[end[0]] > node[0] + end[1]:
                dist[end[0]] = node[0] + end[1]
                heapq.heappush(heap_queue, [dist[end[0]], end[0]])
    return dist


input = lambda: sys.stdin.readline().strip()
N, M, X = map(int, input().split())
adj = collections.defaultdict(list)
for _ in range(M):
    s, e, t = map(int, input().split())
    adj[s].append([e, t])

answer = 0
dist_X = dijkstra(X)
for i in range(1, N+1):
    if i != X:
        answer = max(answer, dijkstra(i)[X] + dist_X[i])
print(answer)