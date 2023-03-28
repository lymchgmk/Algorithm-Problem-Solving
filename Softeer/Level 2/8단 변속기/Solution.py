import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline

    transmission = list(map(int, input().split()))
    if transmission == list(range(1, 9)):
        print("ascending")
    elif transmission == list(range(8, 0, -1)):
        print("descending")
    else:
        print("mixed")

