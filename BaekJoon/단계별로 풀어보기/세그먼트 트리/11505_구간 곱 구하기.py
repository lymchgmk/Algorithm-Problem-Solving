import sys
from math import ceil, log2
sys.stdin = open("11505_구간 곱 구하기.txt", "rt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.height = int(ceil(log2(N)))
        self.tree = [0] * (1 << (self.height + 1))

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            self.tree[node] = (self.build(2*node, start, mid) * self.build(2*node+1, mid+1, end)) % MOD
        return self.tree[node]

    def update(self, node, start, end, idx, val):
        if not (start <= idx <= end):
            return self.tree[node]

        if start == end:
            self.tree[node] = val % MOD
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = (self.update(2*node, start, mid, idx, val) * self.update(2*node+1, mid+1, end, idx, val)) % MOD
        return self.tree[node]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 1

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return (self.query(2*node, start, mid, left, right) * self.query(2*node+1, mid+1, end, left, right)) % MOD


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    MOD = 1000000007
    segment_tree = SegmentTree(arr)
    segment_tree.build(1, 0, N-1)
    for _ in range(M+K):
        a, b, c = map(int, input().split())
        if a == 1:
            segment_tree.update(1, 0, N-1, b-1, c)
        else:
            print(segment_tree.query(1, 0, N-1, b-1, c-1))
