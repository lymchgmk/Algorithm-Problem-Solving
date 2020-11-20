import sys
sys.stdin = open("2805_나무 자르기.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
TREE = list(map(int, input().split()))
s, e = 1, max(TREE)
while s <= e:
    m = (s+e)//2
    wood = sum([tree-m if tree-m > 0 else 0 for tree in TREE])

    if wood >= M:
        s = m + 1
    else:
        e = m - 1

print(e)