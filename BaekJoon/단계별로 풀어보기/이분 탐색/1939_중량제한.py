import sys
from collections import deque
sys.stdin = open("1939_중량제한.txt", "rt")


def bfs(start, end, pass_w):
    dq = deque([start])
    visited = [True] + [False] * N
    visited[start] = True
    while dq:
        curr = dq.popleft()
        for post, w in graph[curr]:
            if not visited[post] and pass_w <= w:
                visited[post] = True
                dq.append(post)
    return visited[end]


def binary_search():
    min_w, max_w = 0, 1000000000
    res_w = min_w
    while min_w <= max_w:
        mid_w = (min_w + max_w) // 2
        if bfs(start, end, mid_w):
            res_w = mid_w
            min_w = mid_w + 1
        else:
            max_w = mid_w - 1
    return res_w


def solution(N, graph, start, end):
    answer = binary_search()
    print(answer)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, M = map(int, input().split())
    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
    start, end = map(int, input().split())
    solution(N, graph, start, end)
