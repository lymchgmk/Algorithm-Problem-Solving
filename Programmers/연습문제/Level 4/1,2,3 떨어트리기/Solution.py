from collections import deque


def solution(edges, target):
    ROOT_NODE, MAX_NODE = 0, len(edges)
    tree = make_tree(edges, ROOT_NODE, MAX_NODE)
    card_orders = {i: [] for i in range(ROOT_NODE, MAX_NODE + 1)}
    for card_index in range(sum(target)):
        tree, card_orders = hand_out_card(card_index, tree, card_orders)
        if can_make_sum(card_orders, target):
            return calc_result(card_orders, target)

    return [-1]


def make_tree(edges, root_node, max_node):
    tree = {i: [] for i in range(root_node, max_node + 1)}
    for s, e in edges:
        tree[s - 1].append(e - 1)

    for node, child in tree.items():
        tree[node] = deque(sorted(child))

    return tree


def find_leaf_nodes(tree):
    leaf_nodes = []
    for node, child in tree.items():
        if len(child) == 0:
            leaf_nodes.append(node)

    return leaf_nodes


def hand_out_card(card_index, tree, card_orders, root_node=0):
    stack = [root_node]
    while stack:
        curr_node = stack.pop()
        curr_child = tree[curr_node]

        if len(curr_child) == 0:
            card_orders[curr_node].append(card_index)
            return tree, card_orders

        post_node = curr_child[0]
        stack.append(post_node)
        tree[curr_node].rotate(-1)


def can_make_sum(card_orders, target):
    for node, card_order in card_orders.items():
        if not (len(card_order) <= target[node] <= len(card_order) * 3):
            return False

    return True


def calc_result(card_orders, target):
    result = []
    for card_order in card_orders.values():
        result += [0] * len(card_order)

    for node, card_order in card_orders.items():
        card_list = create_list_with_max_3(target[node], len(card_order))
        for index, card in zip(card_order, card_list):
            result[index] += card

    return result


def create_list_with_max_3(number, length):
    result = [1] * length
    number -= length
    index = length - 1

    while 0 < number:
        if 2 <= number:
            number -= 2
            result[index] += 2
            index -= 1
        else:
            number -= 1
            result[index] += 1
            index -= 1

    return result


if __name__ == "__main__":
    # edges = [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]]
    # target = [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
    # result = [1, 1, 2, 2, 2, 3, 3]

    edges = [[1, 2], [1, 3]]
    target = [0, 7, 3]
    result = [1, 1, 3, 2, 3]
    answer = solution(edges, target)
    print(answer == result, answer)
