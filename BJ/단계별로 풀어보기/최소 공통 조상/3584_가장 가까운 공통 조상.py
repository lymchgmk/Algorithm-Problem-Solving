import sys
from collections import defaultdict
sys.stdin = open("3584_가장 가까운 공통 조상.txt")
input = lambda: sys.stdin.readline().strip()


T = int(input())
for _ in range(T):
    N = int(input())
    parent = defaultdict(int)
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A

    X, Y = map(int, input().split())
    X_parents, Y_parents = [0, X], [0, Y]
    while parent[X]:
        X_parents.append(parent[X])
        X = parent[X]
    while parent[Y]:
        Y_parents.append(parent[Y])
        Y = parent[Y]

    cnt = 1
    while X_parents[-cnt] == Y_parents[-cnt]:
        cnt += 1
    print(X_parents[-cnt+1])
