import sys
sys.stdin = open("1647_도시 분할 계획.txt", 'rt')


def solution(V, E, adj):
    def find_set(x):
        if p[x] == x:
            return x
        else:
            p[x] = find_set(p[x])
            return p[x]

    def union(x, y):
        px, py = find_set(x), find_set(y)
        if rank[px] > rank[py]:
            p[py] = px
        else:
            p[px] = py
            if rank[px] == rank[py]:
                rank[py] += 1

    p = [i for i in range(N+1)]
    rank = [0] * (N+1)
    cnt = 0
    result = 0
    mst = []
    max_cost = 0
    for s, e, c in graph:
        if cnt == N-1:
            break

        if find_set(s) != find_set(e):
            result += c
            mst.append([s, e, c])
            union(s, e)
            cnt += 1
            max_cost = max(max_cost, c)
    return result - max_cost


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]
    graph.sort(key=lambda x: x[2])
    print(solution(N, M, graph))
