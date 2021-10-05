def count_nodes(root, n, tree):
    cnt = 0
    stack = [root]
    visited = [True] + [False] * n
    while stack:
        parent = stack.pop()
        children = tree[parent]
        for child in children:
            if not visited[child]:
                stack.append(child)
                cnt += 1
                visited[child] = True
    return cnt if cnt else 1


def solution(n, wires):
    tree = {i: [] for i in range(1, n+1)}
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)

    result = n
    for root in range(1, n+1):
        for cand in tree[root]:
            tree[root].remove(cand)
            tree[cand].remove(root)
            cnt_root = count_nodes(root, n, tree)
            cnt_cand = count_nodes(cand, n, tree)
            result = min(result, abs(cnt_root - cnt_cand))
            tree[root].append(cand)
            tree[cand].append(root)
    return result


if __name__ == "__main__":
    # tc 1
    # n = 9
    # wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    # print(solution(n, wires))

    # tc 2
    n = 4
    wires = [[1, 2], [2, 3], [2, 4]]
    print(solution(n, wires))