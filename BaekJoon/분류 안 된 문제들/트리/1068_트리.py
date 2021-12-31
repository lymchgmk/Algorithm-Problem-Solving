import sys
sys.stdin = open('1068_트리.txt', 'r')


class Node:
    def __init__(self, parent=None, child=[]):
        self.parent = parent
        self.child = []


input = lambda: sys.stdin.readline().strip()
N = int(input())
parents = list(map(int, input().split()))
erase_node = int(input())

tree = [Node() for _ in range(N)]
for idx, val in enumerate(parents):
    tree[idx].parent = val
    if val != -1:
        tree[val].child.append(idx)

if tree[erase_node].parent == -1:
    pass
else:
    tree[tree[erase_node].parent].child.remove(erase_node)
tree[erase_node].parent = None
stack = tree[erase_node].child
while stack:
    temp = stack.pop()
    tree[temp].parent = None
    stack.extend(tree[temp].child)

cnt = 0
for node in tree:
    if node.parent != None and not node.child:
        cnt += 1
print(cnt)

for node in tree:
    print(node.parent, node.child)
