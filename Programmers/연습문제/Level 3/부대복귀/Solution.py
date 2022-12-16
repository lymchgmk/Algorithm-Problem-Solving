import heapq


def solution(n, roads, sources, destination):
    adj = {i: [] for i in range(1, n+1)}
    for s, e, in roads:
        adj[s].append([e, 1])
        adj[e].append([s, 1])

    INF = float('inf')
    dist = [INF] * (n+1)
    dist[destination] = 0

    heap_queue = []
    heapq.heappush(heap_queue, [0, destination])
    while heap_queue:
        node = heapq.heappop(heap_queue)
        for end in adj[node[1]]:
            if dist[end[0]] > node[0] + end[1]:
                dist[end[0]] = node[0] + end[1]
                heapq.heappush(heap_queue, [dist[end[0]], end[0]])

    answer = []
    for source in sources:
        if dist[source] == INF:
            answer.append(-1)
        else:
            answer.append(dist[source])
    return answer


if __name__ == "__main__":
    n = 3
    roads = [[1, 2], [2, 3]]
    sources = [2, 3]
    destination = 1
    print(solution(n, roads, sources, destination))
