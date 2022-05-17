from collections import defaultdict


def solution(n, path, order):
    graph = defaultdict(list)
    for path_s, path_e in path:
        graph[path_s].append(path_e)
        graph[path_e].append(path_s)
    
    before = defaultdict(int)
    for order_s, order_e in order:
        if order_e == 0:
            return False
        else:
            before[order_e] = order_s
    
    stack = [0]
    visited = [False] * n
    after = defaultdict(int)
    while stack:
        curr = stack.pop()
        if (curr in before) and (not visited[before[curr]]):
            after[before[curr]] = curr
            continue
        
        visited[curr] = True
        for adj in graph[curr]:
            if not visited[adj]:
                stack.append(adj)
        
        if curr in after:
            stack.append(after[curr])
    
    return all(visited)


n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print(solution(n, path, order))
