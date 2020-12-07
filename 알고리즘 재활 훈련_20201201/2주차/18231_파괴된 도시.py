import sys
sys.stdin = open('18231_파괴된 도시.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


def powerset(lst):
    L = len(lst)
    masks = [1<<i for i in range(L)]
    for i in range(1<<L):
        yield [x for mask, x in zip(masks, lst) if i&mask]


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split())
    adj_list[U].append(V)
    adj_list[V].append(U)

K = int(input())
destroyed = list(map(int, input().split()))
for ps_d in powerset(destroyed):
    test = set()
    for d in ps_d:
        for a in adj_list[d]:
            test.add(a)

    if set(test) == set(destroyed):
        print(len(ps_d))
        print(*ps_d)
        break

else:
    print(-1)