import sys
from collections import defaultdict
import heapq
sys.stdin = open("1197_최소 스패닝 트리.txt", 'rt')


# prim
def solution(V, E, adj):
    visited = {i: False for i in adj.keys()}
    visited[1] = True
    cands = adj[1]
    heapq.heapify(cands)
    total_weight = 0
    while cands:
        weight, end = heapq.heappop(cands)
        if not visited[end]:
            visited[end] = True
            total_weight += weight
            for post_w, post_end in adj[end]:
                if not visited[post_end]:
                    heapq.heappush(cands, [post_w, post_end])
    return total_weight


if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(E):
        A, B, C = map(int, input().split())
        adj[A].append([C, B])
        adj[B].append([C, A])
    print(solution(V, E, adj))
