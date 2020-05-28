import sys
sys.stdin = open("5251_최소 이동 거리.txt")

T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())
    N += 1
    adj = {i: [] for i in range(N)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])

    INF = float('inf')
    dist = [INF] * N
    selected = [False] * N

    dist[0] = 0
    cnt = 0
    while cnt < N:
        # dist가 최소인 정점 찾기
        min = INF
        u = -1
        for i in range(N):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i
        # 결정
        selected[u] = True
        cnt += 1
        # 간선완화
        for w, cost in adj[u]:
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    answer = dist[-1]
    print(f'#{test_case} {answer}')