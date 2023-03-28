import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    T = int(input())
    for case in range(1, T+1):
        A, B = map(int, input().split())
        print(f"Case #{case}: {A + B}")