import sys
from collections import deque
sys.stdin = open("1325_효율적인 해킹.txt", "rt")


def solution(N, M, adj):
    def BFS(start):
        dq = deque()
        dq.append(start)
        visited = [False] * (N + 1)
        visited[start] = True
        while dq:
            curr = dq.popleft()
            for post in adj[curr]:
                if not visited[post]:
                    visited[post] = True
                    dq.append(post)
        return sum(visited)

    counts = [0] * (N + 1)
    for start in range(1, N + 1):
        counts[start] = BFS(start)

    max_cnt = max(counts)
    for i in range(1, N + 1):
        if counts[i] == max_cnt:
            print(i, end=" ")


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        s, e = map(int, input().split())
        adj[e].append(s)

    solution(N, M, adj)
