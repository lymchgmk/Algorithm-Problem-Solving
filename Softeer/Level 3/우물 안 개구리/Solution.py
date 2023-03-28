import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N, M = map(int, input().split())
    W = [0] + list(map(int, input().split()))
    isStrongest = [False] + [True] * N
    for _ in range(M):
        A, B = map(int, input().split())
        if W[A] < W[B]:
            isStrongest[A] = False
        elif W[A] > W[B]:
            isStrongest[B] = False
        else:
            isStrongest[A] = isStrongest[B] = False

    print(sum(isStrongest))
