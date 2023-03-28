import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    A, B = map(int, input().split())
    if A == B:
        print("same")
    else:
        print('A' if A > B else 'B')
