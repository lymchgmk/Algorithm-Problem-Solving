from typing import List
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        
        
# 풀이 1. 중위 순회로 노드 값 누적
class Solution:
    val: int = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
            
        return root