import sys
import math
sys.stdin = open("7469_K번째 수.txt", "rt")


class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.L = len(data)
        self.tree = [0] * 2 * self._size(self.L)
        self.build(1, 0, self.L-1)

    def _size(self, L):
        size = 1
        while size < L:
            size *= 2
        return size

    def build(self, node, left, right):
        if left == right:
            self.tree[node] = self.data[left]
        else:
            mid = (left + right) // 2
            self.tree[node] = self.build(2 * node, left, mid) + self.build(2 * node + 1, mid + 1, right)
        return self.tree[node]


def solution(arr, i, j, k):
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    n, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    segment_tree = SegmentTree(arr)
    print(segment_tree.tree)
    for _ in range(Q):
        i, j, k = map(int, input().split())
        solution(arr, i, j, k)
