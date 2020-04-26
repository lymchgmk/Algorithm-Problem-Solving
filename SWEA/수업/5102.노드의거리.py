import sys, collections
sys.stdin = open("5102.노드의거리.txt", "r")

def bfs(start):
    global result
    deq = collections.deque()
    deq.append(start)
    result.append(start)
    visited[start] = 1

    while deq:
        temp = deq.popleft()

        if visited[G] == 1:
            return distance[G]

        for w in range(1, V+1):
            if adj_matrix[temp][w] == 1 and visited[w] == 0:
                deq.append(w)
                visited[w] = 1
                distance[w] = distance[temp] + 1
                result.append(w)

    return 0


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [0 for _ in range(V+1)]
    adj_matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    distance = [0 for _ in range(V+1)]
    result = []

    for i in range(len(graph)):
        adj_matrix[graph[i][0]][graph[i][1]] = 1
        adj_matrix[graph[i][1]][graph[i][0]] = 1

    print("#{} {}".format(test_case, bfs(S)))