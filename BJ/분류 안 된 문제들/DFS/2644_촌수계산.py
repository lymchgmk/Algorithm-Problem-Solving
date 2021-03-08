import sys
sys.stdin = open('2644_촌수계산.txt', 'r')
import collections


def bfs(start):
    deq = collections.deque()
    deq.append(start)
    visited = [0]*(n+1)
    visited[start] = 1
    while deq:
        pop = deq.popleft()
        for next in family[pop]:
            if visited[next] == 0:
                visited[next] = 1
                result[next] = result[pop] + 1
                deq.append(next)
    

input = lambda: sys.stdin.readline().strip()
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
family = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

result = [0]*(n+1)
bfs(p1)
print(result[p2] if result[p2] != 0 else -1)
