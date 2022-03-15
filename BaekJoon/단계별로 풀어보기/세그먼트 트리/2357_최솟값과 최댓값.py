import sys
from typing import *
from math import ceil, log2
sys.stdin = open("2357_최솟값과 최댓값.txt", "rt")


class SegmentTree:
    def __init__(self):
        pass

    def build(self):
        pass

    def query(self, node, left, right, start, end) -> List[int, int]:
        pass


def solution(arr, ab):
    segment_tree = SegmentTree()
    for a, b in ab:
        print(*segment_tree.query(1, 0, N-1, a, b))


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    ab = [list(map(int, input().split())) for _ in range(M)]
    solution(arr, ab)
