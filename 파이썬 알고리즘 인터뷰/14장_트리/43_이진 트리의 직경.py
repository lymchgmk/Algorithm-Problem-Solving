# 풀이 1. 상태값 누적 트리 DFS


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None
        self.parent = None
        
        
class Solution:
    longest: int = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1
        
        dfs(root)
        
        return self.longest
    