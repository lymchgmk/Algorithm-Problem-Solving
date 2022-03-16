import sys
from math import ceil, log2
from bisect import bisect_right
sys.setrecursionlimit(10**9)
sys.stdin = open("7469_K번째 수.txt", "rt")


class MergeSortTree:
    def __init__(self, data):
        self.data = data
        self.data_len = len(data)
        self.tree_height = int(ceil(log2(self.data_len)))
        self.tree = [[]] * (1 << (self.tree_height + 1))

    def build(self, node, left, right):
        if left == right:
            self.tree[node] = [self.data[left]]
            return self.tree[node]

        mid = (left + right) // 2
        left_arr = self.build(2 * node, left, mid)
        right_arr = self.build(2 * node + 1, mid + 1, right)
        self.tree[node] = self._merge(left_arr, right_arr)
        return self.tree[node]

    def _merge(self, left_arr, right_arr):
        merged_arr = []
        i, j = 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1
        while i < len(left_arr):
            merged_arr.append(left_arr[i])
            i += 1
        while j < len(right_arr):
            merged_arr.append(right_arr[j])
            j += 1
        return merged_arr

    def query(self, target, node, left, right, start, end):
        if start <= left and right <= end:
            return bisect_right(self.tree[node], target)
        if end < left or right < start:
            return 0
        mid = (left + right) // 2
        return self.query(target, 2*node, left, mid, start, end) + self.query(target, 2*node+1, mid+1, right, start, end)


def solution(n, m, arr, Q):
    tree = MergeSortTree(arr)
    tree.build(1, 0, n-1)
    for i, j, k in Q:
        left, right = int(-1e9), int(1e9)
        while left <= right:
            mid = (left + right) // 2
            cnt = tree.query(mid, 1, 0, n-1, i-1, j-1)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        print(left)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(m)]
    solution(n, m, arr, Q)

