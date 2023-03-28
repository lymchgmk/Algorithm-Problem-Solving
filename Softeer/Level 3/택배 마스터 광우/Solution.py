import sys
from itertools import permutations


def solution(rails):
    curr_w = total_w = 0
    idx = 0
    for _ in range(K):
        while curr_w + rails[idx] <= M:
            curr_w += rails[idx]
            idx = (idx + 1) % N

        total_w += curr_w
        curr_w = 0

    return total_w


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N, M, K = map(int, input().split())
    boxes = list(map(int, input().split()))

    answer = float('inf')
    for rails in permutations(boxes):
        answer = min(answer, solution(rails))

    print(answer)
