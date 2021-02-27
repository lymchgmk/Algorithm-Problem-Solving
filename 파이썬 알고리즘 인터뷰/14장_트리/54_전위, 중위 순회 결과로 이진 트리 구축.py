from typing import List
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        
        
# 풀이 1. 전위 순회 결과로 중위 순회 분할 정복
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        # 전위 순회 결과는 중위 순회 분할 인덱스
        index = inorder.index(preorder.pop(0))
        
        # 중위 순회 결과 분할 정복
        node = TreeNode(inorder[index])
        node.left = self.buildTree(preorder, inorder[0:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])
        
        return node
    
    return None