import sys
from math import ceil, log2
sys.stdin = open("2243_사탕상자.txt", "rt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        height = int(ceil(log2(N)))
        self.tree = [0] * (1 << (height + 1))
        self.build(1, 0, N-1)

    def build(self, node, start, end):
        pass

    def update(self, node, start, end, idx, val):
        pass

    def query(self, node, start, end, left, right):
        pass

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    segment_tree = SegmentTree()
    for _ in range(n):
        A, *cmd = map(int, input().split())
        if A == 1:
            B = cmd[0]
            print(segment_tree.query())
        else:
            B, C = cmd[0], cmd[1]
            segment_tree.update()

