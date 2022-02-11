import sys
from collections import deque
sys.stdin = open("1158_요세푸스 문제.txt", "rt")


def solution(N, K):
    dq = deque([n for n in range(1, N + 1)])
    answer = []
    while dq:
        dq.rotate(-K + 1)
        answer.append(dq.popleft())
    return "<" + ", ".join(map(str, answer)) + ">"


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, K = map(int, input().split())
    print(solution(N, K))
