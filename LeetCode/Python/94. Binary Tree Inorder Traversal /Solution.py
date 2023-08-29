# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []

        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            inorder_list.append(node.val)
            inorder(node.right)

        inorder(root)

        return inorder_list