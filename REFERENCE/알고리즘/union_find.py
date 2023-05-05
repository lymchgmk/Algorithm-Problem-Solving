def find(target):
    if parent(target) != target:
        return find(parent[target])

    return target


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b