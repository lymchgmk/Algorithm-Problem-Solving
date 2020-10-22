import sys
sys.stdin = open('2164_카드2.txt', 'rt')


from collections import deque


N = int(input())
deq = deque()
for i in range(1, N+1):
    deq.append(i)

while len(deq) != 1:
    deq.popleft()
    if len(deq) == 1:
        break
    deq.append(deq.popleft())

print(deq[0])
