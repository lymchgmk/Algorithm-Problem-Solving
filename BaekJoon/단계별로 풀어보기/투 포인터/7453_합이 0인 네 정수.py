import sys
from collections import Counter
sys.stdin = open("7453_합이 0인 네 정수.txt", "rt")


def solution(N, A, B, C, D):
    AB, CD = [], []
    for i in range(N):
        for j in range(N):
            AB.append(A[i] + B[j])
            CD.append(-(C[i] + D[j]))

    answer = 0
    cntr = Counter(CD)
    for num in AB:
        answer += cntr[num]
    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
    solution(N, A, B, C, D)
