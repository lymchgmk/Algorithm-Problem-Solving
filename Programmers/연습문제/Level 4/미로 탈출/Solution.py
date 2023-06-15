from heapq import heappush, heappop

INF = float('inf')


def solution(n, start, end, roads, traps):
    graph = {i: [] for i in range(1, n+1)}
    for s, e, w in roads:
        graph[s].append([e, w])
        graph[e].append([s, -w])

    traps = {trap: idx for trap, idx in enumerate(traps)}

    dists = [[INF] * (2 ** len(traps)) for _ in range(n+1)]
    hq = []
    start_node, start_dist, start_state = 1, 0, 0
    heappush(hq, [start_dist, start_node, start_state])
    while hq:
        curr_dist, curr_node, curr_state = heappop(hq)
        curr_mask =

        for post_node, post_dist in graph[curr_node]:





if __name__ == "__main__":
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    result = 4
    answer = solution(n, start, end, roads, traps)
    print(result == answer, answer)