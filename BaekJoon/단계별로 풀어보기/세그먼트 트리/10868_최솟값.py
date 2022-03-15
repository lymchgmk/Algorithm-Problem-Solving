import sys
from math import ceil, log2
sys.stdin = open("10868_최솟값.txt", "rt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * (1 << (int(ceil(log2(N))) + 1))
        self.build(1, 0, N - 1)

    def build(self, node, left, right):
        if left == right:
            self.tree[node] = self.data[left]
        else:
            mid = (left + right) // 2
            self.tree[node] = min(self.build(2*node, left, mid), self.build(2*node+1, mid+1, right))
        return self.tree[node]

    def query(self, node, left, right, start, end):
        if start <= left and right <= end:
            return self.tree[node]

        if left > end or right < start:
            return float('inf')

        mid = (left + right) // 2
        return min(self.query(2*node, left, mid, start, end), self.query(2*node+1, mid+1, right, start, end))


def solution(arr, ab):
    segment_tree = SegmentTree(arr)
    for a, b in ab:
        print(segment_tree.query(1, 0, N-1, a-1, b-1))


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    ab = [list(map(int, input().split())) for _ in range(M)]
    solution(arr, ab)
