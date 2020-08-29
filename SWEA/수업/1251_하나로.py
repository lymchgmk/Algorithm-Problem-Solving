import sys
sys.stdin = open("1251_하나로.txt")


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    adj = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            adj[i][j] = (X[i]-X[j])**2 + (Y[i]-Y[j])**2

    INF = float('inf')
    key = [INF] * N
    p = [-1] * N
    mst = [False] * N

    key[0] = 0
    cnt = 0
    result = 0
    while cnt < N:
        min = INF
        u = -1
        for i in range(N):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i
                break
        mst[u] = True
        result += min
        cnt += 1

        for w in range(N):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u

    answer = round(result*E)
    print(f'#{test_case} {answer}')