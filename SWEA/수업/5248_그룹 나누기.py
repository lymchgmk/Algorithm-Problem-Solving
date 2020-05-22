import sys
sys.stdin = open('5248_그룹나누기.txt', 'r')

from collections import deque

def bfs(n):
    global result
    queue = deque()
    queue.append(n)
    visited[n] = 1
    while queue:
        temp = queue.popleft()
        for tmp in adj_matrix[temp]:
            if not visited[tmp]:
                visited[tmp] = 1
                queue.append(tmp)
    return 1

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * (N + 1)
    adj_matrix = [[] for _ in range(N + 1)]
    data = list(map(int, input().split()))

    for idx in range(M):
        adj_matrix[data[idx * 2]].append(data[idx * 2 + 1])
        adj_matrix[data[idx * 2 + 1]].append(data[idx * 2])

    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            result += bfs(i)

    print(f'#{test_case} {result}')