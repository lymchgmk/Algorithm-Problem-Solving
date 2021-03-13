import sys
sys.stdin = open('12851_숨바꼭질 2.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


N, K = map(int, input().strip().split())
MAX = 100000 + 1
INF = float('inf')
DP = [[INF, 0] for _ in range(MAX)]
DP[N] = [0, 1]
deq = deque([N])
while deq:
    now = deq.popleft()
    test = [2*now, now-1, now+1]
    for new in test:
        if 0<=new<MAX:
            # 처음 그 지점에 도달하는 경우
            if DP[new][0] == INF:
                deq.append(new)
                DP[new][0] = DP[now][0] + 1
                DP[new][1] = DP[now][1]
            # 처음이 아닌 경우지만 최소시간만에 도달하는 경우
            elif DP[new][0] == DP[now][0] + 1:
                DP[new][1] += DP[now][1]

print(DP[K][0])
print(DP[K][1])