def dfs(v):
    # global G, visited, V
    visited[v] = 1
    print(v, end=" ")

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("dfs_input.txt")
V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화
visited = [0 for i in range(V+1)]

for i in range(0, len(temp), 2):  #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):  #입력확인
    print("{} {}".format(i, G[i]))

dfs(1)

