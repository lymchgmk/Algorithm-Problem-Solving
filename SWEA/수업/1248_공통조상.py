import sys
sys.stdin = open("1248_공통조상.txt")


def find_fathers(S, adj):
    fathers = [S]
    root = []

    while fathers:
        child = fathers.pop()
        for key, val in adj.items():
            if child in val:
                fathers.append(key)
                root.append(key)
                break
    return root


def find_common_father(fathers1, fathers2):
    for father in fathers1:
        if father in fathers2:
            return father


def dfs(start, graph):
    visit=[]
    stack=[start]

    while stack:
        node = stack.pop()
        if node not in graph.keys():
            visit.append(node)
            continue
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit


T = int(input())

for test_case in range(1, T+1):
    V, E, S1, S2 = map(int, input().split())
    data = list(map(int, input().split()))

    adj_dict = {}
    for i in range(E):
        if data[2*i] not in adj_dict.keys():
            adj_dict.setdefault(data[2 * i], [data[2 * i + 1]])
        else:
            temp = adj_dict[data[2 * i]].append(data[2 * i + 1])
            adj_dict.setdefault(data[2 * i], temp)

    S1_fathers = find_fathers(S1, adj_dict)
    S2_fathers = find_fathers(S2, adj_dict)

    common_father = find_common_father(S1_fathers, S2_fathers)
    subtree_length = len(dfs(common_father, adj_dict))

    print(f'#{test_case} {common_father} {subtree_length}')
