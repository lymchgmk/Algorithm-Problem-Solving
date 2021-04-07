preorder_list = []
def preorder(node, nodeinfo):
    preorder_list.append(node.index)
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)


inorder_list = []
def inorder(node, nodeinfo):
    if node.left:
        inorder(node.left, nodeinfo)
    inorder_list.append(node.index)
    if node.right:
        inorder(node.right, nodeinfo)


postorder_list = []
def postorder(node, nodeinfo):
    if node.left:
        postorder(node.left, nodeinfo)
    if node.right:
        postorder(node.right, nodeinfo)
    postorder_list.append(node.index)