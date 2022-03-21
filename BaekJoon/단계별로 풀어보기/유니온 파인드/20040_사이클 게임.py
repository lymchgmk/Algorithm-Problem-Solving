import sys
sys.stdin = open("20040_사이클 게임.txt", "rt")
input = lambda: sys.stdin.readline().strip()


def find(target):
    if target == parents[target]:
        return target
    else:
        parents[target] = find(parents[target])
        return parents[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    n, m = map(int, input().split())
    parents = [p for p in range(n)]
    for i in range(1, m+1):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(i)
            break
        union(a, b)
    else:
        print(0)
