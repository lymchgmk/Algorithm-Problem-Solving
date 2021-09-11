import sys
sys.stdin = open('15681_트리와 쿼리.txt', 'r')
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)


def count_node(parent):
    node_count[parent] = 1
    for child in tree[parent]:
        if not node_count[child]:
            count_node(child)
            node_count[parent] += node_count[child]


N, R, Q = map(int, input().split())
tree = {i+1: [] for i in range(N)}
node_count = [0] * (N+1)
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

count_node(R)

for _ in range(Q):
    node = int(input())
    print(node_count[node])
