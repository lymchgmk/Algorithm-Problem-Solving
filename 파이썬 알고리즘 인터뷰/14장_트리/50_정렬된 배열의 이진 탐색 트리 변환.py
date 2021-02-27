from typing import List
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = 0
        
        
# 풀이 1. 이진 검색 결과로 트리 구성
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None
    
    mid = len(nums) // 2
    
    # 분할 정복으로 이진 검색 결과 트리 구성
    node = TreeNode(nums[mid])
    node.left = self.sortedArrayToBST(nums[:mid])
    node.right = self.sortedArrayToBST(nums[mid+1:])
    
    return node