import sys
sys.stdin = open('1991_트리 순회.txt', 'r')


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    print(node.val, end= '')
    if node.left != '.': preorder(tree[node.left])
    if node.right != '.': preorder(tree[node.right])


def inorder(node):
    if node.left != '.': inorder(tree[node.left])
    print(node.val, end= '')
    if node.right != '.': inorder(tree[node.right])


def postorder(node):
    if node.left != '.': postorder(tree[node.left])
    if node.right != '.': postorder(tree[node.right])
    print(node.val, end= '')
    
    
input = lambda: sys.stdin.readline().strip()
N = int(input())
tree = {}
for _ in range(N):
    val, left, right = input().split()
    tree[val] = Node(val, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])