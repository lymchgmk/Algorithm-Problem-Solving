import sys
sys.stdin = open("11657_타임머신.txt", "rt")
input = lambda: sys.stdin.readline().strip()


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

if not isUpdated:
    print(-1)
else:
    for d in dist[2:]:
        print(d if d != INF else -1)