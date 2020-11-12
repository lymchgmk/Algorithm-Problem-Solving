import sys
sys.stdin = open('10866_덱.txt', 'rt')


from collections import deque


input = sys.stdin.readline
N = int(input())
deq = deque()
for _ in range(N):
    X = list(input().split())
    if X[0] == 'push_front':
        deq.appendleft(X[1])
    elif X[0] =='push_back':
        deq.append(X[1])
    elif X[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif X[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif X[0] == 'size':
        print(len(deq))
    elif X[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif X[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif X[0] == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)