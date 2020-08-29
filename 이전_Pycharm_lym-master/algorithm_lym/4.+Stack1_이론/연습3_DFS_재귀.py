'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # global G, visited, V
    visited[v] = 1
    print(v, end=" ")

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

import sys
sys.stdin = open("연습3_input.txt")
V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)] for j in range(V+1)] #2차원 초기화
visited = [0 for i in range(V+1)]

# 인접행렬로 저장
for i in range(0, len(temp), 2):  #입력
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

# 입력확인
for i in range(V+1):
    print("{} {}".format(i, G[i]))

dfs(1)

