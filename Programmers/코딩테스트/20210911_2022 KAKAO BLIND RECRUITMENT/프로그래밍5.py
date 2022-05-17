from collections import defaultdict


class Node:
    def __init__(self):
        self.parent = None
        self.children = []


def solution(info, edges):
    graph = {idx: Node() for idx in range(N)}
    for s, e in edges:
        graph[s].children.append(e)
        graph[e].parent = s

    DP = {i: [0, 0] for i in range(N)}
    for idx, val in enumerate(info):
        if val == 0:
            DP[idx][0] += 1
        else:
            DP[idx][1] += 1

    start = 0
    children = graph[start].children
    while children:
        for child in children:
            if


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges)) # 5
