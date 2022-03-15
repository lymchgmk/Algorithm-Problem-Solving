import sys
from bisect import bisect_left
sys.stdin = open("1965_상자넣기.txt", "rt")


def solution(N, boxes):
    LIS = [0]
    for box in boxes:
        if LIS[-1] < box:
            LIS.append(box)
        else:
            idx = bisect_left(LIS, box)
            LIS[idx] = box
    print(len(LIS) - 1)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    boxes = list(map(int, input().split()))
    solution(N, boxes)
