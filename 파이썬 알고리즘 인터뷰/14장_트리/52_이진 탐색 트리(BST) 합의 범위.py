from typing import List
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = 0
        
        
# 풀이 1. 재귀 구조 DFS로 브루트 포스 탐색
def rangeSumBST_1(self, root: TreeNode, L: int, R: int) -> int:
    if not root: return 0;
    
    return (root.val if L <= root.val <= R else 0) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)


# 풀이 2. DFS 가지치기로 필요한 노드 탐색
def rangeSumBST_2(self, root: TreeNode, L: int, R: int) -> int:
    def dfs(node: TreeNode):
        if not node:
            return 0
        
        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        
        return node.val + dfs(node.left) + dfs(node.right)
    
    return dfs(root)


# 풀이 3. 반복 구조 DFS로 필요한 노드 탐색

def rangeSUmBST(self, root: TreeNode, L: int, R: int) -> int:
    stack, num = [root], 0
    # 스택 이용 필요한 노드 DFS 반복
    while stack:
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    
    return sum


# 풀이 4. 반복 구조 BFS로 필요한 노드 탐색
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    stack, sum = [root], 0
    # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
    while stack:
        node = stack.pop(0)
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
        
    return sum
