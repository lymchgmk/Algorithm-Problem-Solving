import heapq


def solution(N, road, K):
    adj = {i: [] for i in range(N+1)}
    for r in road:
        start, end, cost = r
        adj[start].append([end, cost])
        adj[end].append([start, cost])
    
    INF = float('inf')
    dist = [INF]*(N+1)
    dist[1] = 0
    
    hq = []
    heapq.heappush(hq, [0, 1])
    while hq:
        now_cost, now = heapq.heappop(hq)
        for next, next_cost in adj[now]:
            if dist[next] > now_cost + next_cost:
                dist[next] = now_cost + next_cost
                heapq.heappush(hq, [dist[next], next])
                
    answer = 0
    for d in dist:
        if d <= K:
            answer += 1
            
    return answer


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))
