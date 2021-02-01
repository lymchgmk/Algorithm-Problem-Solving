import sys
sys.stdin = open("1956_운동.txt", "rt")
input = lambda: sys.stdin.readline().strip()

V, E = map(int, input().split())
INF = float('inf')
dist = [[INF]*V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

result = INF
for i in range(V):
    result = min(result, dist[i][i])

if result == INF:
    print(-1)
else:
    print(result)