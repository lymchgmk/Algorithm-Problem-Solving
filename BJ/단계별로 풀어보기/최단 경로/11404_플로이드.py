import sys
sys.stdin = open("11404_플로이드.txt", "rt")
input = lambda: sys.stdin.readline().strip()


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