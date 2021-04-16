from collections import deque, defaultdict


def solution(a, edges):
    class TreeNode:
        def __init__(self, key, val):
            self.key = key
            self.value = val
            self.parent = None
            self.child = None
        
    if sum(a):
        return -1
    
    answer = 0
    # 1. 트리 만들기
    Tree = []
    for v1, v2 in edges:
        Tree.append()
        
    # 1-1. p1이 이미 다른 노드를 가리키면, p2가 p1을 가리키도록
    
    # 2. 리프노드만 찾아서 처리
    
    # 3. 다 처리
    if not any(a):
        return answer
    else:
        return -1


a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
