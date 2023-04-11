from collections import defaultdict


def solution(n, lighthouse):
    tree = makeTree(lighthouse)
    visited = [False] * (n+1)
    start_node = 1

    return min(dfs(start_node, tree, visited))


def makeTree(lighthouse):
    _tree = defaultdict(list)

    for n1, n2 in lighthouse:
        _tree[n1].append(n2)
        _tree[n2].append(n1)

    return _tree


def dfs(parent_node, tree, visited):
    visited[parent_node] = True
    on, off = 1, 0
    child_nodes = filter(lambda x: not visited[x], tree[parent_node])
    for child_node in child_nodes:
        pick, not_pick = dfs(child_node, tree, visited)
        on += min(pick, not_pick)
        off += pick

    return on, off


if __name__ == "__main__":
    n = 8
    lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]
    result = 2
    answer = solution(n, lighthouse)
    print(f"[{answer == result}]: {answer}")
