import sys
from math import ceil, log2
sys.stdin = open("2268_수들의 합 7.txt", "rt")
sys.setrecursionlimit(10**9)


class SegmentTree:
    def __init__(self):
        # _height = int(ceil(log2(N)))
        # self.tree = [0] * (1 << (_height + 1))
        self.tree = [0] * (4*N)

    def modify(self, node, start, end, idx, val):
        if not (start <= idx <= end):
            return self.tree[node]

        if start == end:
            self.tree[node] = val
            return val

        mid = (start + end) // 2
        self.tree[node] = self.modify(2*node, start, mid, idx, val) + self.modify(2*node+1, mid+1, end, idx, val)
        return self.tree[node]

    def sum(self, node, start, end, left, right):
        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self.sum(2*node, start, mid, left, right) + self.sum(2*node+1, mid+1, end, left, right)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    segment_tree = SegmentTree()
    for _ in range(M):
        cmd, i, j = map(int, input().split())
        if cmd == 0:
            if i > j:
                i, j = j, i
            print(segment_tree.sum(1, 0, N-1, i-1, j-1))
        elif cmd == 1:
            segment_tree.modify(1, 0, N-1, i-1, j)
