import sys
sys.stdin = open("13913_숨바꼭질 4.txt")
input = lambda: sys.stdin.readline().strip()

from collections import deque


N, K = map(int, input().split())
visited = [0] * 1000001
path = [0] * 1000001

deq = deque([N])
while deq:
    curr = deq.popleft()
    if curr == K:
        print(visited[K])
        p = []
        while curr != N:
            p.append(curr)
            curr = path[curr]
        p.append(N)
        p.reverse()
        print(*p)
        break

    for post in (curr+1, curr-1, 2*curr):
        if 0<=post<1000001 and not visited[post]:
            visited[post] = visited[curr] + 1
            path[post] = curr
            deq.append(post)




