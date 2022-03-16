import sys
from math import ceil, log2
sys.stdin = open("1275_커피숍2.txt", "rt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        height = int(ceil(log2(N)))
        self.tree = [0] * (1 << (height + 1))
        self.build(1, 0, N-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.build(2*node, start, mid) + self.build(2*node+1, mid+1, end)
        return self.tree[node]

    def update(self, node, start, end, idx, val):
        if not (start <= idx <= end):
            return self.tree[node]

        if start == end:
            self.tree[node] += val
            return self.tree[node]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.update(2*node, start, mid, idx, val) + self.update(2*node+1, mid+1, end, idx, val)
            return self.tree[node]

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            return self.query(2*node, start, mid, left, right) + self.query(2*node+1, mid+1, end, left, right)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    segment_tree = SegmentTree(arr)
    print(segment_tree.tree)
    for _ in range(Q):
        x, y, a, b = map(int, input().split())
        if x < y:
            print(segment_tree.query(1, 0, N-1, x-1, y-1))
        else:
            print(segment_tree.query(1, 0, N-1, y-1, x-1))
        segment_tree.update(1, 0, N-1, a-1, b)

