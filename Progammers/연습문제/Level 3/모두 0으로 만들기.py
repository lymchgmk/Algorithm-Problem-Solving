def solution(a, edges):
    class Node:
        def __init__(self):
            self.parent = None
    
    if sum(a):
        return -1
    
    tree = {idx: Node() for idx, val in enumerate(a)}
    for key1, key2 in edges:
        if not tree[key1].parent:
            tree[key1].parent = key2
        else:
            old_parent = tree[key1].parent
            tree[old_parent].parent = key1
            tree[key1].parent = key2

    for key in tree:
        if tree[key].parent is None:
            root = tree[key]
    
    answer = 0
    while root.child:
        for key in tree:
            if not tree[key].child:
                tree[tree[key].parent].child.remove(key)
                answer += abs(a[key])
                a[tree[key].parent] += a[key]
                a[key] = 0
            
    if not any(a):
        return answer
    else:
        return -1


a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))