import sys
from math import ceil, log2
sys.stdin = open("14438_수열과 쿼리 17.txt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.height = int(ceil(log2(N)))
        self.tree = [0] * (1 << (self.height + 1))

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_build = self.build(2*node, start, mid)
            right_build = self.build(2*node+1, mid+1, end)
            self.tree[node] = min(left_build, right_build)
            return self.tree[node]

    def update(self, node, start, end, idx, val):
        if not (start <= idx <= end):
            return self.tree[node]

        if start == end:
            self.tree[node] = val
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_update = self.update(2*node, start, mid, idx, val)
            right_update = self.update(2*node+1, mid+1, end, idx, val)
            self.tree[node] = min(left_update, right_update)
            return self.tree[node]

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return float('inf')

        if left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_query = self.query(2*node, start, mid, left, right)
            right_query = self.query(2*node+1, mid+1, end, left, right)
            return min(left_query, right_query)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    A = list(map(int, input().split()))
    segment_tree = SegmentTree(A)
    segment_tree.build(1, 0, N-1)
    M = int(input())
    for _ in range(M):
        cmd, i, j = map(int, input().split())
        if cmd == 1:
            segment_tree.update(1, 0, N-1, i-1, j)
        elif cmd == 2:
            print(segment_tree.query(1, 0, N-1, i-1, j-1))
