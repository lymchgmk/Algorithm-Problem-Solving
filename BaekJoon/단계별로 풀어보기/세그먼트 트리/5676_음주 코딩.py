import sys
from math import ceil, log2
sys.stdin = open("5676_음주 코딩.txt", "rt")
sys.setrecursionlimit(10*9)


class SegmentTree:
    def __init__(self, N, data):
        self.data = data
        self.height = int(ceil(log2(N)))
        self.tree = [0] * (1 << (self.height + 1))
        self.build(1, 0, N-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_build = self.build(2*node, start, mid)
            right_build = self.build(2*node+1, mid+1, end)
            self.tree[node] = left_build * right_build
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
            self.tree[node] = left_update * right_update
            return self.tree[node]

    def query(self, node, start, end, left, right):
        print(node, start, end, left, right)
        if start > right or end < left:
            return 1

        if left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (left + right) // 2
            left_query = self.query(2*node, start, mid, left, right)
            right_query = self.query(2*node+1, mid+1, end, left, right)
            return left_query * right_query


def trim(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, K = map(int, input().split())
    X = []
    for num in map(int, input().split()):
        X.append(trim(num))

    segment_tree = SegmentTree(N, X)
    for _ in range(K):
        CP, *cmd = input().split()
        if CP == 'C':
            idx, val = map(int, cmd)
            val = trim(val)
            segment_tree.update(1, 0, N-1, idx-1, val)
        elif CP == 'P':
            i, j = map(int, cmd)
            print(i, j)
            res = segment_tree.query(1, 0, N-1, i-1, j-1)

