import sys
from math import ceil, log2
sys.stdin = open("10999_구간 합 구하기 2.txt", "rt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        _height = int(ceil(log2(N)))
        self.tree = [0] * (1 << (_height + 1))
        self.lazy = [0] * (1 << (_height + 1))
        self.build(1, 0, N-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.build(2*node, start, mid) + self.build(2*node+1, mid+1, end)
            return self.tree[node]

    def _lazy_propagate(self, node, start, end):
        if self.lazy[node] != 0:
            if start != end:
                self.lazy[2*node] += self.lazy[node]
                self.lazy[2*node+1] += self.lazy[node]
            self.tree[node] += self.lazy[node] * (end - start + 1)
            self.lazy[node] = 0

    def update(self, node, start, end, left, right, val):
        self._lazy_propagate(node, start, end)

        if start > right or end < left:
            return self.tree[node]

        if left <= start and end <= right:
            self.lazy[node] = val
            self._lazy_propagate(node, start, end)
            return self.tree[node]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.update(2*node, start, mid, left, right, val) + self.update(2*node+1, mid+1, end, left, right, val)
            return self.tree[node]

    def query(self, node, start, end, left, right):
        self._lazy_propagate(node, start, end)

        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            return self.query(2*node, start, mid, left, right) + self.query(2*node+1, mid+1, end, left, right)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    segment_tree = SegmentTree(arr)
    for _ in range(M+K):
        a, *cmd = map(int, input().split())
        if a == 1:
            b, c, d = cmd
            segment_tree.update(1, 0, N-1, b-1, c-1, d)
        else:
            b, c = cmd
            print(segment_tree.query(1, 0, N-1, b-1, c-1))
