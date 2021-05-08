import heapq


def solution(n, start, end, roads, traps):
    # key에서 나가고, 들어오고
    go_out = {key: [] for key in range(1, n + 1)}
    come_in = {key: [] for key in range(1, n + 1)}
    for s, e, d in roads:
        go_out[s].append([e, d])
        come_in[e].append([s, d])
    print(go_out)
    print(come_in)

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap_queue = []
    # 처음에
    heapq.heappush(heap_queue, [0, start, go_out, come_in])
    while heap_queue:
        curr_dist, curr_node, curr_go_out, curr_come_in = heapq.heappop(heap_queue)
        for post_node, post_dist in curr_go_out[curr_node]:
            if dist[post_node] > curr_dist + post_dist:
                dist[post_node] = curr_dist + post_dist
                post_go_out, post_come_in = curr_go_out.copy(), curr_come_in.copy()
                if post_node in traps:
                    post_out, post_in = post_maze[post_node]
                    post_maze[post_node] = [post_in, post_out]
    #                 for key in post_out:
    #                     key_out, key_in = post_maze[key]
    #                     key_out[post_node] = key_in[post_node]
    #                     del key_in[post_node]
    #
    #                 for key in post_in:
    #                     key_out, key_in = post_maze[key]
    #                     key_in[post_node] = key_out[post_node]
    #                     del key_out[post_node]
    #
    #             print(post_maze)
    #
    #
    #             heapq.heappush(heap_queue, [dist[post_node], post_node, post_maze])
    #
    # return dist


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))  # 5
