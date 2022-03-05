import sys
sys.stdin = open('18352_특정 거리의 도시 찾기.txt', 'rt')
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


def solution(N, M, K, X, graph):
    dists_res = dijkstra(X, graph)
    ans = []
    for city, dist in dists_res.items():
        if dist == K:
            ans.append(city)
    if ans:
        ans.sort()
        for a in ans:
            print(a)
    else:
        print(-1)


if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    graph = {i: defaultdict(dict) for i in range(1, N+1)}
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A][B] = 1
    solution(N, M, K, X, graph)
