import sys
from math import ceil, log2
sys.stdin = open("1725_히스토그램.txt", "rt")
sys.setrecursionlimit(10**9)


class SegmentTree:
    def __init__(self):
        self.tree_h = int(ceil(log2(N)))
        self.tree = [0] * (1 << (self.tree_h + 1))

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = start
        else:
            mid = (start + end) // 2
            left_idx = self.build(2*node, start, mid)
            right_idx = self.build(2*node + 1, mid+1, end)
            if H[left_idx] <= H[right_idx]:
                self.tree[node] = left_idx
            else:
                self.tree[node] = right_idx
        return self.tree[node]

    def find_min_h_idx(self, node, start, end, left, right):
        RANGEOUT = -1
        if left > end or right < start:
            return RANGEOUT
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_min_h_idx = self.find_min_h_idx(2*node, start, mid, left, right)
        right_min_h_idx = self.find_min_h_idx(2*node+1, mid+1, end, left, right)
        if left_min_h_idx == RANGEOUT:
            return right_min_h_idx
        if right_min_h_idx == RANGEOUT:
            return left_min_h_idx
        left_min_h, right_min_h = H[left_min_h_idx], H[right_min_h_idx]
        if left_min_h <= right_min_h:
            return left_min_h_idx
        else:
            return right_min_h_idx

    def max_area(self, left, right):
        min_h_idx = self.find_min_h_idx(1, 0, N-1, left, right)
        min_h = H[min_h_idx]
        area = (right - left + 1) * min_h
        # print(H)
        # print(f'left: {left}, right: {right}, min_h_idx: {min_h_idx}, min_h: {min_h}, area: {area}')
        if left <= min_h_idx - 1:
            left_area = self.max_area(left, min_h_idx-1)
            area = max(area, left_area)
        if min_h_idx + 1 <= right:
            right_area = self.max_area(min_h_idx+1, right)
            area = max(area, right_area)
        return area


def solution(N, H):
    segment_tree = SegmentTree()
    segment_tree.build(1, 0, N-1)
    print(segment_tree.max_area(0, N-1))


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    H = [int(input()) for _ in range(N)]
    solution(N, H)
