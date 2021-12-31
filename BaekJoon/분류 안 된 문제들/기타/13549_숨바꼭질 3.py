import sys
sys.stdin = open('13549_숨바꼭질 3.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


N, K = map(int, input().strip().split())
MAX = 100000 + 1
time = [-1]*MAX
time[N] = 0
deq = deque([N])
while deq:
    now = deq.popleft()
    test = [2*now, now-1, now+1]
    for new in test:
        if 0<=new<MAX and time[new] == -1:
            if new == 2*now:
                deq.appendleft(new)
                time[new] = time[now]
            else:
                deq.append(new)
                time[new] = time[now]+1

print(time[K])