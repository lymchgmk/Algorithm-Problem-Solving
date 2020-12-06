def find(target):
    if target == parent[target]:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a