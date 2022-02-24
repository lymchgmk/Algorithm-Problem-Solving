import sys
from collections import deque
sys.stdin = open('2252_줄 세우기.txt', 'rt')

# 위상 정렬 topology sort
def solution(N, M, indegree, graph):
    result = []
    dq = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        curr = dq.popleft()
        result.append(curr)
        for post in graph[curr]:
            indegree[post] -= 1
            if indegree[post] == 0:
                dq.append(post)

    print(*result)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        indegree[B] += 1
    solution(N, M, indegree, graph)
