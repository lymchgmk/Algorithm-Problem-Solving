'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(G, v):
    visited = [0] * (V+1)
    q = []

    q.append(v)
    visited[v] = 1
    print(v, end=" ")

    while len(q) != 0:
        v = q.pop(0)
        for w in range(V+1):
            if G[v][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = 1
                print(w, end=" ")

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화

for i in range(0, len(temp), 2):  #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):  #입력확인
    print("{} {}".format(i, G[i]))

bfs(G, 1)

