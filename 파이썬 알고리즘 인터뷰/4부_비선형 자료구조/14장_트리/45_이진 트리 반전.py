import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


# 풀이 1. 파이썬다운 방식
def invertTree_1(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree_1(root.right), self.invertTree_1(root.left)
        return root
    
    else:
        return None
    
    
# 풀이 2. 반복 구조로 BFS
def invertTree_2(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
    
    return root


# 풀이 3. 반복 구조로 DFS
def invertTree_3(self, root: TreeNode) -> TreeNode:
    stack = []
    
    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            stack.append(node.right)
            stack.append(node.left)
            
    return root


# 풀이 4. 반복 구조로 DFS 후위 순회
def invertTree_4(self, root: TreeNode) -> TreeNode:
    stack = []
    
    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            stack.append(node.right)
            stack.append(node.left)
            
            # 후위 순회!
            node.left, node.right = node.right, node.left
    
    return root