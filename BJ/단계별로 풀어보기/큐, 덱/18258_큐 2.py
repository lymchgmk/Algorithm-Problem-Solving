import sys
sys.stdin = open('18258_큐 2.txt', 'rt')


from collections import deque



N = int(input())
deq = deque()
for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'push':
        deq.append(int(command[1]))
    elif command[0] == 'pop':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])