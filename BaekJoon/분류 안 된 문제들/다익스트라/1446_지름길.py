import sys
sys.stdin = open('1446_지름길.txt', 'rt')
from collections import defaultdict
import heapq


def dijkstra(start, _graph):
    dists = {node: float('inf') for node in range(1, N+1)}
    dists[start] = 0
    q = []
    heapq.heappush(q, [dists[start], start])
    while q:
        curr_dist, curr_dest = heapq.heappop(q)

        if dists[curr_dest] < curr_dist:
            continue

        for post_dest, post_dist in _graph[curr_dest].items():
            _dist = curr_dist + post_dist
            if _dist < dists[post_dest]:
                dists[post_dest] = _dist
                heapq.heappush(q, [_dist, post_dest])
    return dists




if __name__ == "__main__":
    N, D = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(N):
        S, E, dist = map(int, input().split())
        graph[S][E] = dist
    print(graph)
    # solution(N, D, graph)
