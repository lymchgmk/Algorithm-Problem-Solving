import sys
sys.stdin = open("5247_연산.txt")

from collections import deque

def bfs(N, M):
    global queue
    visited[N] = 1

    while queue:
        temp = queue.popleft()
        val, cnt = temp[0], temp[1]

        for idx in range(4):
            if idx != 3:
                operated_val = val + operations[idx]
            else:
                operated_val = 2 * val

            if operated_val == M:
                return cnt

            if 1 <= operated_val <= 1000000 and visited[operated_val] == 0:
                visited[operated_val] = 1
                queue.append((operated_val, cnt + 1))

T=int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    operations = (+1, -1, -10)

    queue = deque()
    queue.append([N, 1])
    visited = [0] * (1000000 + 1)

    answer = bfs(N, M)

    print(f'#{test_case} {answer}')