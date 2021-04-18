import sys
sys.setrecursionlimit(100000)


def solution(a, edges):
    if sum(a) != 0:
        return -1

    graph = {idx: [] for idx in range(len(a))}
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    def dfs(cur, root):
        nonlocal answer
        for nxt in graph[cur]:
            if nxt != root:
                dfs(nxt, cur)
        a[root] += a[cur]
        answer += abs(a[cur])
        a[cur] = 0
        
    answer = 0
    dfs(0, 0)

    return answer
    
    
a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
