import sys


def power(a, n):
    if n == 0:
        return 1

    x = power(a, n // 2) % DIV

    if n % 2 == 0:
        return (x * x) % DIV
    else:
        return (x * x * a) % DIV


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    K, P, N = map(int, input().split())
    DIV = 1_000_000_007

    print(K * power(P, 10 * N) % DIV)
