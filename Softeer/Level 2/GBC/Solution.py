import sys
from collections import deque


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N, M = map(int, input().split())
    limits = deque(list(map(int, input().split())) for _ in range(N))
    tests = [list(map(int, input().split())) for _ in range(M)]

    for i in range(N-1):
        limits[i+1][0] += limits[i][0]

    for i in range(M-1):
        tests[i+1][0] += tests[i][0]

    answer = 0
    for test_h, test_s in tests:
        while limits and limits[0][0] < test_h:
            answer = max(answer, test_s - limits[0][1])
            limits.popleft()

        if limits and test_h <= limits[0][0]:
            answer = max(answer, test_s - limits[0][1])

        if limits and test_h == limits[0][0]:
            limits.popleft()

    print(answer)
