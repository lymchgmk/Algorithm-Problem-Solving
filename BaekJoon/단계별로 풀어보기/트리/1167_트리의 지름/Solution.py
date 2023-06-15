import sys


if __name__ == "__main__":
    sys.stdin = open("Input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    V = int(input())
    tree = {node: {} for node in range(1, V + 1)}
    for _ in range(V):
        *E, _ = map(int, input().split())
        parent, children = E[0], E[1:]
        for i in range(0, len(children), 2):
            tree[parent][children[i]] = children[i + 1]

    answer_dist = 0
    for start_node in range(1, V + 1):
        stack = [(start_node, 0)]
        while stack:
            curr_node, curr_dist = stack.pop()
            for post_node in tree[curr_node]:

