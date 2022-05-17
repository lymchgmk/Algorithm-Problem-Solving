import sys
sys.setrecursionlimit(10**8)


def solution(nodeinfo):
    class Tree:
        def __init__(self, index, x, y):
            self.index = index
            self.x = x
            self.y = y
            self.left = self.right = None
    
    def preorder(node, nodeinfo):
        preorder_list.append(node.index)
        if node.left:
            preorder(node.left, nodeinfo)
        if node.right:
            preorder(node.right, nodeinfo)
    
    def postorder(node, nodeinfo):
        if node.left:
            postorder(node.left, nodeinfo)
        if node.right:
            postorder(node.right, nodeinfo)
        postorder_list.append(node.index)
    
    preorder_list = []
    postorder_list = []
    nodeinfo_with_idx = [[idx+1] + node for idx, node in enumerate(nodeinfo)]
    nodeinfo_with_idx.sort(key=lambda node: (-node[2], node[1]))

    root = None
    for node in nodeinfo_with_idx:
        if not root:
            root = Tree(*node)
        else:
            idx, x, y = node
            current = root
            while True:
                if x < current.x:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(*node)
                        break
                elif x > current.x:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(*node)
                        break
                break

    preorder(root, nodeinfo)
    postorder(root, nodeinfo)

    return [preorder_list, postorder_list]


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))