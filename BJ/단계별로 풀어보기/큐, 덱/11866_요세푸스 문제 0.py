import sys
sys.stdin = open('11866_요세푸스 문제 0.txt', 'rt')


from collections import deque


N, K = map(int, input().split())
deq = deque([i+1 for i in range(N)])
answer = []
while deq:
    for i in range(K-1):
        deq.append(deq.popleft())
    answer.append(deq.popleft())

print("<", end = '')
print(*answer, sep = ", ", end = '')
print(">", end = '')

            
