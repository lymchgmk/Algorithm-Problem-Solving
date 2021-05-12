import sys
sys.stdin = open('1922_네트워크 연결.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


def union(x, y):
    px, py = find_set(x), find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1
            

            
N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(M)]
graph.sort(key=lambda x: x[2])


p = [n for n in range(N+1)]
rank = [0] * (N+1)
cnt = 0
result = 0
mst = []
for s, e, c in graph:
    if cnt == N-1:
        break

    if find_set(s) != find_set(e):
        result += c
        mst.append([s, e, c])
        union(s, e)
        cnt += 1
    
print(result)
