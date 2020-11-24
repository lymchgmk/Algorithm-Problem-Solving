import sys
sys.stdin = open('2042_구간 합 구하기.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N, M, K = map(int, input().split())
A = [int(input()) for _ in range(N)]


class SegTree:
    def init(self, node, left, right):
        if left + 1 == right:
            self.tree[node] = self.A[left]
        else:
            mid = (left+right)//2
            self.tree[node] = self.init(node*2, left, mid) + self.init(node*2+1, mid, right)
        return self.tree[node]


    def __init__(self, N, A):
        self.A = A
        self.tree = [0]*4*N
        self.init(1, 0, N)

    
    def sum(self, node, left, right, start, end):
        if start <= left and right <= end:
            return self.tree[node]
        if right <= start or end <= left:
            return 0
        mid = (left+right)//2
        return self.sum(node*2, left, mid, start, end) + self.sum(node*2+1, mid, right, start, end)


    def update(self, node, left, right, target, value):
        if left <= target < right:
            self.tree[node] += value
            if left + 1 == right:
                return
            mid = (left+right)//2
            self.update(node*2, left, mid, target, value)
            self.update(node*2+1, mid, right, target, value)


ST = SegTree(N, A)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 2:
        print(ST.sum(1, 0, N, b, c))
    else:
        ST.update(1, 0, N, b, c-ST.A[b])
        ST.A[b] = c