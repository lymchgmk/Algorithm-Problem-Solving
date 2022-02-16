class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def solution(info, edges):
    L = len(info)
    def make_tree():
        _tree = {i: Node(i) for i in range(L)}
        for parent, child in edges:
            _tree[child].parent = parent
            if _tree[parent].left is None:
                _tree[parent].left = child
            else:
                _tree[parent].right = child
        return _tree
        #
        # for i in range(L):
        #     print(tree[i].data, tree[i].left, tree[i].right, info[i])
    def dfs():
        stack = [0]
        while stack:
            curr = stack.pop()
            curr_parent = tree[curr].parent
            curr_left, curr_right = tree[curr].left, tree[curr].right

    tree = make_tree()


if __name__ == "__main__":
    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
    print(solution(info, edges))