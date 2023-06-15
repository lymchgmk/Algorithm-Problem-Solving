from collections import defaultdict


def solution(edges, target):
    ROOT_NODE = 1
    MAX_NODE = len(edges) + 1

    tree = {i: [0, []] for i in range(ROOT_NODE, MAX_NODE + 1)}
    for s, e in edges:
        tree[s][1].append(e)

    for node in range(ROOT_NODE, MAX_NODE + 1):
        tree[node][1].sort()

    counts = {i: 0 for i in range(ROOT_NODE, MAX_NODE + 1)}

    for _ in range(10):
        print(counts)

        curr_node = ROOT_NODE
        while 0 < len(tree[curr_node][1]):
            curr_idx = tree[curr_node][0]
            tree[curr_node][0] = (tree[curr_node][0] + 1) % len(tree[curr_node][1])
            curr_node = tree[curr_node][1][curr_idx]

        counts[curr_node] += 1


def can_pass(target, counts):
    for i in range(1, len(target) + 1):
        if not (counts[i] <= target[i - 1] <= counts[i] * 3):
            return False

    return True




if __name__ == "__main__":
    edges = [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]]
    target = [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
    result = [1, 1, 2, 2, 2, 3, 3]
    answer = solution(edges, target)
    print(answer == result, answer)
