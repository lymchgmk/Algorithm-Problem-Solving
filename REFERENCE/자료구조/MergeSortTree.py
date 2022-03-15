from math import ceil, log2


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
        left_arr = self.build(2*node, left, mid)
        right_arr = self.build(2*node+1, mid+1, right)
        self.tree[node] = self.merge(left_arr, right_arr)
        return self.tree[node]

    def merge(self, left_arr, right_arr):
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
