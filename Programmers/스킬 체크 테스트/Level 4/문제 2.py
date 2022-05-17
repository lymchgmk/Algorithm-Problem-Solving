import collections


def solution(n, edges):
    def BFS(start):
        visited = [False]*(n+1)
        deq = collections.deque([start])
        while deq:
            now = deq.popleft()
            for next in adj[now]:
                if not visited[next]:
                    visited
    
    adj = [[] for _ in range(n)]
    for s, e in edges:
        adj[s].append([e, 1])
        adj[e].append([s, 1])
    return answer


n = 4
edges = [[1,2],[2,3],[3,4]]
print(solution(n, edges))