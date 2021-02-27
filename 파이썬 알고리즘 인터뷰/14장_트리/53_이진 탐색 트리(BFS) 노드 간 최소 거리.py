from typing import List
import collections
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        
        
# 풀이 1. 재귀 구조로 중위 순회
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
    

# 풀이 2. 반복 구조로 중위 순회
def minDiffInBST(self, root: TreeNode) -> int:
    prev = -sys.maxsize
    result = sys.maxsize
    
    stack = []
    node = root
    
    # 반복 구조 중위 순회 비교 결과
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        result = min(result, node.val - prev)
        prev = node.val
        
        node = node.right
        
    return result
