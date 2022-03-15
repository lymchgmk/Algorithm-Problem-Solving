import sys
from math import ceil, log2
sys.stdin = open("2357_최솟값과 최댓값.txt", "rt")
sys.setrecursionlimit(10**9)


class SegmentTree:
    MIN, MAX = 0, 1000000000

    def __init__(self, data):
        self.data = data
        tree_height = int(ceil(log2(N)))
        self.tree = [[SegmentTree.MAX, SegmentTree.MIN]] * (1 << (tree_height + 1))
        self._build(1, 0, N-1)

    def _build(self, node, left, right):
        if left == right:
            self.tree[node] = [self.data[left], self.data[left]]
        else:
            mid = (left + right) // 2
            min_left, max_left = self._build(2*node, left, mid)
            min_right, max_right = self._build(2*node+1, mid+1, right)
            self.tree[node] = [min(min_left, min_right), max(max_left, max_right)]
        return self.tree[node]

    def query(self, node, left, right, start, end):
        if start <= left and right <= end:
            return self.tree[node]

        if left > end or right < start:
            return [SegmentTree.MAX, SegmentTree.MIN]

        mid = (left + right) // 2
        min_left, max_left = self.query(2*node, left, mid, start, end)
        min_right, max_right = self.query(2*node+1, mid+1, right, start, end)
        return [min(min_left, min_right), max(max_left, max_right)]


def solution(arr, ab):
    segment_tree = SegmentTree(arr)
    for a, b in ab:
        print(*segment_tree.query(1, 0, N-1, a-1, b-1))


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    ab = [list(map(int, input().split())) for _ in range(M)]
    solution(arr, ab)
