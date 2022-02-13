import sys
from heapdict import heapdict
sys.stdin = open("1197_최소 스패닝 트리.txt", 'rt')


# prim
def solution(V, E, graph, start):
    hd, updates, total_weight = heapdict(), dict(), 0
    for node in graph.keys():
        hd[node] = float('inf')
        updates[node] = None

    hd[start], updates[start] = 0, start
    while hd:
        curr_node, curr_weight = hd.popitem()
        total_weight += curr_weight
        for adj_node, adj_weight in graph[curr_node].items():
            if adj_node in hd and adj_weight < hd[adj_node]:
                hd[adj_node] = adj_weight
                updates[adj_node] = curr_node
    return total_weight


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = {i: {} for i in range(1, V+1)}
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A][B] = graph[B][A] = C
    print(solution(V, E, graph, 1))

