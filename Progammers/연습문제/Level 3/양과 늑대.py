class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None
        self.left = None
        self.right = None


def solution(info, edges):
    def make_tree():
        _tree = {i: Node(i) for i in range(L)}
        for parent, child in edges:
            _tree[child].parent = parent
            if _tree[parent].left is None:
                _tree[parent].left = child
            else:
                _tree[parent].right = child
        return _tree

    def dfs():
        stack = []
        start_idx, start_s_w = 0, {0: 1, 1: 0}
        start_cands = set()
        start_cands.add(tree[start_idx].left)
        start_cands.add(tree[start_idx].right)
        max_sheep = 1
        stack.append((start_idx, start_s_w, start_cands))
        while stack:
            curr_idx, curr_s_w, curr_cands = stack.pop()
            curr_left, curr_right = tree[curr_idx].left, tree[curr_idx].right
            if curr_left is not None:
                curr_cands.add(curr_left)
            if curr_right is not None:
                curr_cands.add(curr_right)

            for post_idx in curr_cands:
                post_s_w = curr_s_w.copy()
                post_s_w[info[post_idx]] += 1
                if post_s_w[0] > post_s_w[1]:
                    post_cands = curr_cands.copy()
                    post_cands.remove(post_idx)
                    max_sheep = max(max_sheep, post_s_w[0])
                    stack.append((post_idx, post_s_w, post_cands))
        return max_sheep

    L = len(info)
    tree = make_tree()
    return dfs()


if __name__ == "__main__":
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    print(solution(info, edges))