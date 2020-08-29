import sys
sys.stdin = open("A_test.txt", "rt", encoding="UTF8")

def my_dfs(adj_matrix, visited, S):
    visited[S] = 1
    global my_node
    my_node.append(S)

    for w in range(V+1):
        if adj_matrix[S][w] == 1 and visited[w] == 0:
            my_dfs(adj_matrix, visited, w)

    return my_node


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V: 정점(node) 수 / E: 간선 수
    adj_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    my_node = []
    ans = 0

    for e in range(E):
        data = list(map(int, input().split()))

        adj_matrix[data[0]][data[1]] = 1
        adj_matrix[data[1]][data[0]] = 1

    S, G = map(int, input().split())

    if G in (my_dfs(adj_matrix, visited, S)):
        ans = 1

    print("#{} {}".format(test_case, ans))
