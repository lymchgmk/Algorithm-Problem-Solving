import sys
from collections import defaultdict, Counter
sys.stdin = open("4195_친구 네트워크.txt", "rt")


def find(target):
    if not parent[target]:
        cntr[target] = 1
        parent[target] = target
        return target

    if target == parent[target]:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a
        cntr[a] += cntr[b]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()

    T = int(input())
    for _ in range(T):
        F = int(input())
        parent = defaultdict(str)
        cntr = Counter()
        for _ in range(F):
            A, B = sorted(input().split())
            union(A, B)
            print(cntr[parent[A]])
