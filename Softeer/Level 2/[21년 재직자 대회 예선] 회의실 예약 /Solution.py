import sys
from collections import deque


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    M, N, K = map(int, input().split())
    secret = deque(map(int, input().split()))
    controls = list(map(int, input().split()))
    target = deque(controls[:len(secret)])
    result = "normal"
    for i in range(len(secret), len(controls)):
        if target == secret:
            result = "secret"
            break

        target.popleft()
        target.append(controls[i])

    print(result if target != secret else "secret")
