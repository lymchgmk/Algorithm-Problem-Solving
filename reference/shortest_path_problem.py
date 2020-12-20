# 1. 단일-출발 최단 경로 문제
# 2. 단일-도착 최단 경로 문제
# 3. 전체-쌍 최단 경로 문제

# 데이크스트라 알고리즘 : 단일-쌍, 단일-출발, 단일-도착

# 벨먼-포드 알고리즘 : 가중치가 음수라면 단일-출발
def bellman_ford():
    global isUpdated

    for repeat in range(N):
        for i in range(1, N+1):
            for b, c in adj[i]:
                if dist[i] != INF and dist[b] > dist[i] + c:
                    dist[b] = dist[i] + c
                    if repeat == N-1:
                        isUpdated = False
    
    return


N, M = map(int, input().split())
INF = float('inf')
dist = [INF]*(N+1)
dist[1] = 0
isUpdated = True

adj = {i:[] for i in range(N+1)}
for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append([B, C])

bellman_ford()

# A* 탐색 알고리즘 : 탐색 속도 향상을 위한 휴리스틱 방법, 단일-쌍

# 플로이드-와셜 알고리즘 : 전체-쌍
def floyd_warshall():
    global dist

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j != k and dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]
    
    return dist


n = int(input())
m = int(input())
INF = float('inf')
dist = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(lambda x: int(x)-1, input().split())
    c += 1
    dist[a][b] = min(dist[a][b], c)

ans = floyd_warshall()
for i in range(n):
    for j in range(n):
        if ans[i][j] == INF:
            ans[i][j] = 0
    print(*ans[i])