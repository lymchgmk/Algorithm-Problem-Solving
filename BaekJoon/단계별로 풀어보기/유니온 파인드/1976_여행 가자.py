import sys
sys.stdin = open("1976_여행 가자.txt", "rt")
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


N = int(input())
M = int(input())
parent = {i: i for i in range(1, N+1)}

for i in range(1, N+1):
    adj_matrix = list(map(int, input().split()))
    for j in range(1, len(adj_matrix)+1):
        if adj_matrix[j-1] == 1:
            union(i, j)

travel_plan = list(map(int, input().split()))
result = set([find(i) for i in travel_plan])

if len(result) == 1:
    print("YES")
else:
    print("NO")