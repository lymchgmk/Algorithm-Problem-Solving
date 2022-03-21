import sys
sys.stdin = open("16562_친구비.txt", "r")


def find(target):
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def min_cost(i):
    cost = A[i-1]
    for j in range(1, N+1):
        if i != j and find(i) == find(j):
            visited[j] = True
            cost = min(cost, A[j-1])
    return cost


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, M, k = map(int, input().split())
    A = list(map(int, input().split()))
    parent = {n: n for n in range(1, N+1)}
    for _ in range(M):
        v, w = map(int, input().split())
        union(v, w)

    answer = 0
    visited = {n: False for n in range(1, N+1)}
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            answer += min_cost(i)
    print(answer if answer <= k else "Oh no")
