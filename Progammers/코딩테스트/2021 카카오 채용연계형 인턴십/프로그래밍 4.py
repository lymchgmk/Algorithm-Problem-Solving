import heapq


def solution(n, start, end, roads, traps):
    # False: 정상, True: 트랩작동 후
    maze = {key: {False: [], True: []} for key in range(1, n+1)}
    for s, e, d in roads:
        maze[s][False].append([d, e])
        maze[e][True].append([d, s])
    
    print(maze)
    
    INF = float('inf')
    dist = [INF]*(n+1)
    dist[start] = 0
    heap_queue = []
    # 처음에는 다 작동 안됨
    heapq.heappush(heap_queue, [0, start, {i: False for i in range(1, n+1)}])
    while heap_queue:
        curr_dist, curr_node, curr_activated_traps = heapq.heappop(heap_queue)
        curr_maze = {}
        for key in curr_activated_traps:
            curr_maze[key] = maze[key][curr_activated_traps[key]]
        print(curr_node, curr_maze)

        for post_dist, post_node in curr_maze[curr_node]:
            if dist[post_node] > curr_dist + post_dist:
                dist[post_node] = curr_dist + post_dist
                post_activated_traps = curr_activated_traps.copy()
                if post_node in traps:
                    post_activated_traps[post_node] = not post_activated_traps[post_node]
                heapq.heappush(heap_queue, [dist[post_node], post_node, post_activated_traps])

    return dist
    


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps)) # 5
