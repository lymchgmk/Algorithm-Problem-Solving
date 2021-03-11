import sys
sys.stdin = open("1167_트리의 지름.txt", "rt")
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_dst=0, right_dst=0):
        self.val = val
        self.left = left
        self.right = right
        self.left_dst = left_dst
        self.right_dst = right_dst


input = lambda: sys.stdin.readline().strip()
V = int(input())
tree = [[0]*(V+1) for _ in range(V+1)]
for _ in range(V):
    *E, _ = list(map(int, input().split()))
    for i in range(1, len(E), 2):
        tree[E[0]][E[i]] = E[i+1]

longest = float('-inf')
for start in range(1, V+1):
    deq = collections.deque([start])
    temp_longest = 0
    while deq:
        temp = deq.popleft()
        for next in tree[temp]:
            if next != 0:
                temp_longest += next
                