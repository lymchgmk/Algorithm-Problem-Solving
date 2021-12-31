import sys
sys.stdin = open("1717_집합의 표현.txt", "rt")
input = lambda: sys.stdin.readline().strip()


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


n, m = map(int, input().split())
parent = [x for x in range(n+1)]
for _ in range(m):
    zero_one, a, b = map(int, input().split())
    if zero_one == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")