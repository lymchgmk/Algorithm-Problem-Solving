def solution(a, edges):
    def find_leaf(graph):
        return [node for node in graph if len(graph[node]) == 1]
    
    def find_root(graph):
        return max(graph, key=lambda x: len(graph[x]))
    
    def dfs(a):
        answer = 0
        stack = find_leaf(graph)
        root = find_root(graph)
        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if nxt == root:
                    break
                answer += abs(a[cur])
                a[nxt] += a[cur]
                a[cur] = 0
                stack.append(nxt)
                
        return answer
        
    if not any(a):
        return 0
    
    if sum(a):
        return -1
    
    graph = {i: [] for i in range(len(a))}
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return dfs(a)
    
    
a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
