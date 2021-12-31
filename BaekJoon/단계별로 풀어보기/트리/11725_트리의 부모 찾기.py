import sys
sys.stdin = open("11725_트리의 부모 찾기.txt", "rt")
import collections


input = lambda: sys.stdin.readline().strip()
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

parents = [0]*(N+1)

deq = collections.deque([1])
while deq:
    tmp = deq.popleft()
    for i in tree[tmp]:
        if parents[tmp-1] != i:
            parents[i-1] = tmp
            deq.append(i)

for i in parents[1:-1]:
    print(i)

