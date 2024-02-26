def solution(n, edges):
    tree = get_tree(n, edges)
    a_nodes = get_furthest_nodes(1, tree)
    b_nodes = get_furthest_nodes(a_nodes[0], tree)
    max_distance = calc_distance(a_nodes[0], b_nodes[0], tree)

    if len(a_nodes) == 1 and len(b_nodes) == 1:
        return max_distance - 1
    else:
        return max_distance


def get_tree(n, edges):
    tree = {i: [] for i in range(1, n + 1)}
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    return tree


def get_furthest_nodes(start_node, tree):
    stack = [(start_node, 0)]
    visited = {i: False for i in tree}
    furthest_nodes = []
    _max_dist = 0
    while stack:
        curr_node, curr_dist = stack.pop()
        visited[curr_node] = True

        if _max_dist < curr_dist:
            furthest_nodes = [curr_node]
            _max_dist = curr_dist
        elif _max_dist == curr_dist:
            furthest_nodes.append(curr_node)

        for post_node in tree[curr_node]:
            if not visited[post_node]:
                post_dist = curr_dist + 1
                stack.append((post_node, post_dist))

    return furthest_nodes


def calc_distance(start_node, end_node, tree):
    stack = [(start_node, 0)]
    visited = {i: False for i in tree}
    distance = 0
    while stack:
        curr_node, curr_dist = stack.pop()
        visited[curr_node] = True

        if curr_node == end_node:
            return curr_dist

        for post_node in tree[curr_node]:
            if not visited[post_node]:
                post_dist = curr_dist + 1
                stack.append((post_node, post_dist))
