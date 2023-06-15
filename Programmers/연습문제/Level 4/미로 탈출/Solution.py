from heapq import heappush, heappop

INF = float('inf')


def solution(n, start, end, roads, traps):

    def node_is_trap(node, bitmask):
        if node not in traps:
            return False

        return True if (1 << traps[node]) & bitmask else False

    graph = {i: [] for i in range(1, n+1)}
    for s, e, w in roads:
        graph[s].append([e, w])
        graph[e].append([s, -w])

    traps = {trap: idx for idx, trap in enumerate(traps)}

    start_node, start_dist, start_bitmask = start, 0, 0
    dists = [[INF] * (1 << len(traps)) for _ in range(n + 1)]
    dists[start_node][start_bitmask] = 0
    hq = []
    heappush(hq, [start_dist, start_node, start_bitmask])
    while hq:
        curr_dist, curr_node, curr_bitmask = heappop(hq)

        if curr_node == end:
            return dists[curr_node][curr_bitmask]

        for post_node, post_dist in graph[curr_node]:
            post_dist = post_dist if node_is_trap(curr_node, curr_bitmask) == node_is_trap(post_node, curr_bitmask) else post_dist * (-1)
            post_bitmask = curr_bitmask if post_node not in traps else (curr_bitmask ^ (1 << traps[post_node]))

            if 0 < post_dist and dists[post_node][post_bitmask] > curr_dist + post_dist:
                dists[post_node][post_bitmask] = curr_dist + post_dist
                heappush(hq, [curr_dist + post_dist, post_node, post_bitmask])


if __name__ == "__main__":
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    result = 4
    answer = solution(n, start, end, roads, traps)
    print(result == answer, answer)