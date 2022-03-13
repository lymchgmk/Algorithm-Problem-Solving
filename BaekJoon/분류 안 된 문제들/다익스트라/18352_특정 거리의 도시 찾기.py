import sys
from collections import deque
sys.stdin = open('18352_특정 거리의 도시 찾기.txt', 'rt')


def solution(N, M, K, X, graph):
    def bfs(start, K):
        dists, visited = [0] * (N+1), [False] * (N+1)
        dists[start], visited[start] = 0, True
        dq = deque([start])
        res = []
        while dq:
            curr_city = dq.popleft()
            for post_city in graph[curr_city]:
                if not visited[post_city]:
                    visited[post_city] = True
                    dists[post_city] = dists[curr_city] + 1
                    dq.append(post_city)
                    if dists[post_city] == K:
                        res.append(post_city)
        return res

    cities = bfs(X, K)
    cities.sort()
    if not cities:
        print(-1)
    else:
        for city in cities:
            print(city)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, K, X = map(int, input().split())
    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
    solution(N, M, K, X, graph)
