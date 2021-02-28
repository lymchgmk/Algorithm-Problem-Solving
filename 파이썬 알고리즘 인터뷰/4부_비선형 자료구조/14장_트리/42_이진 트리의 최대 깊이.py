import collections


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self._leftChild = None
        self._rightChild = None
        self.parent = None


# 풀이 1. 반복 구조로 BFS 풀이
def maxDepth(self, root: TreeNode) -> int:
    if root is None: 
        return 0

    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    # BFS 반복 횟수 == 깊이
    return depth
