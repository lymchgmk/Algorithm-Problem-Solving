import sys
sys.stdin = open('1697_숨바꼭질.txt', 'rt')


from collections import deque


input = sys.stdin.readline
N, K = map(int, input().strip().split())
visited = [False]* (100000 + 1)


def BFS(v):
    global visited
    cnt = 0
    deq = deque([[v, cnt]])
    while deq:
        temp = deq.popleft()
        test, cnt = temp[0], temp[1]
        if not visited[test]:
            visited[test] = True
            if test == K:
                return cnt
            cnt += 1
            if test-1 >= 0:
                deq.append([test-1, cnt])
            if test+1 <= 100000:
                deq.append([test+1, cnt])
            if 2*test <= 100000:
                deq.append([2*test, cnt])
    return cnt
        

print(BFS(N))