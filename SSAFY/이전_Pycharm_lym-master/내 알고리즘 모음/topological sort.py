def dfs(graph, start):
    path = []
    stack = [start]
    label = len(graph)
    result = {}
    while stack != []:
        for element in stack:
            if element not in result:
                result[element] = label
                label = label - 1

        v = stack.pop()
        if v not in path: path.append(v)
        for w in reversed(graph[v]):
            if w not in path and not w in stack:
                stack.append(w)

    result = {v: k for k, v in result.items()}
    return path, result


T = 10
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    E_list = list(map(int, input().split()))

    data = [0] + [[0] for _ in range(V)]
    for i in range(len(E_list)):
        if i % 2 == 0:
            data[E_list(i)].append(E_list[i + 1])

    data_dict = {}
    for i in range(1, len(data)):
        data_dict[i] = data[i]

    print(data_dict)



# graph = {1: [3], 3: [5, 6], 5: [4], 4: [7], 7: [], 6: []}
# print(*dfs(graph, 1))