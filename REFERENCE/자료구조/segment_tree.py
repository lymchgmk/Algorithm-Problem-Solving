class SegTree:
    def init(self, node, left, right):
        # 리프 노드 인 경우
        if left + 1 == right:
            self.tree[node] = self.A[left]
        # 리프 노드가 아닌 경우
        else:
            mid = (left + right) // 2
            self.tree[node] = self.init(node*2, left, mid) + self.init(node*2 + 1, mid, right)
        
        return self.tree[node]

    def __init__(self, N, A):
        self.A = A
        # 기본적인 트리 크기 정해 줌
        self.tree = [0] * 4 * N
        # 시작 노드
        self.init(1, 0, N)

    # 구간 합
    def sum(self, node, left, right, start, end):
        # [left, right)가 [start, end)에 완전 포함되는 경우
        if start <= left and right <= end:
            return self.tree[node]
        # [left, right)와 [start, end)의 겹치는 부분이 없는 경우
        if right <= start or end <= left:
            return 0
        # [left, right)가 [start, end)에 부분 포함되는 경우
        mid = (left + right) // 2
        return self.sum(node * 2, left, mid, start, end) + self.sum(node * 2 + 1, mid, right, start, end)

    # 값 변경
    def update(self, node, left, right, target, value):
        # target이 [left, right)에 속하는 경우
        if left <= target < right:
            self.tree[node] += value
            # 리프노드인 경우
            if left + 1 == right:
                return
            # 리프노드가 아닌 경우
            mid = (left + right) // 2
            self.update(node * 2, left, mid, target, value)
            self.update(node * 2 + 1, mid, right, target, value)