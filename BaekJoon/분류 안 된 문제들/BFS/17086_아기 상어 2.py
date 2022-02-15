import sys
from collections import deque
sys.stdin = open("17086_아기 상어 2.txt", "rt")


def solution(N, M, arr):
    def bfs(dq):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        while dq:
            curr_r, curr_c = dq.popleft()
            for dir_r, dir_c in dirs:
                post_r, post_c = curr_r + dir_r, curr_c + dir_c
                if 0 <= post_r < N and 0 <= post_c < M:
                    if arr[post_r][post_c] == 0:
                        dq.append((post_r, post_c))
                        arr[post_r][post_c] = arr[curr_r][curr_c] + 1

    dq = deque([(r, c) for r in range(N) for c in range(M) if arr[r][c] == 1])
    bfs(dq)
    answer = 0
    for r in range(N):
        for c in range(M):
            if answer < arr[r][c]:
                answer = arr[r][c]
    print(answer - 1)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solution(N, M, arr)

