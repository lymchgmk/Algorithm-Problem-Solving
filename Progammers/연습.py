import heapq
from copy import deepcopy


def solution(n, start, end, roads, traps):
    # key에서 나가고, 들어오고
    go_out = {key: {} for key in range(1, n + 1)}
    come_in = {key: {} for key in range(1, n + 1)}
    for s, e, d in roads:
        go_out[s][e] = d
        come_in[e][s] = d

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    visited = [False] * (n+1)
    heap_queue = []
    # 처음에
    heapq.heappush(heap_queue, [0, start, go_out, come_in])
    while heap_queue:
        curr_dist, curr_node, curr_go_out, curr_come_in = heapq.heappop(heap_queue)
        visited[curr_node] = True
        for post_node, post_dist in curr_go_out[curr_node].items():
            if not visited[post_node] and dist[post_node] > curr_dist + post_dist:
                dist[post_node] = curr_dist + post_dist
                
                post_go_out, post_come_in = deepcopy(curr_go_out), deepcopy(curr_come_in)
                if post_node in traps:
                    for target, d in post_go_out[post_node].items():
                        post_go_out[target][post_node] = d

                    for target, d in post_come_in[post_node].items():
                        post_come_in[target][post_node] = d

                    post_go_out[post_node], post_come_in[post_node] = post_come_in[post_node], post_go_out[post_node]
                heapq.heappush(heap_queue, [dist[post_node], post_node, post_go_out, post_come_in])
            print(curr_node, post_node, dist)
            print(post_go_out)
            print(post_come_in)
            print()

    return dist


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))  # 5
