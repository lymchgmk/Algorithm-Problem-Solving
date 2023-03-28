import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    K, P, N = map(int, input().split())
    DIV = 1_000_000_007

    while N:
        K = (K * P) % DIV
        N -= 1

    print(K)
