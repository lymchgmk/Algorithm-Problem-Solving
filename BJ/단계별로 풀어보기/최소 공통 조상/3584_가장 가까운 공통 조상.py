import sys
sys.stdin = open("3584_가장 가까운 공통 조상.txt")
input = lambda: sys.stdin.readline().strip()


T = int(input())
for _ in range(T):
    N = int(input())
    tree = {i: [] for i in range(1, N+1)}
    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[A].append(B)

    X, Y = map(int, input().split())

    print(tree)
    print(X, Y)