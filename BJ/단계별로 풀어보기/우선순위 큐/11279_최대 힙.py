import sys
sys.stdin = open('11279_최대 힙.txt', 'rt')


from queue import PriorityQueue

input = lambda: sys.stdin.readline().strip()
N = int(input())
PQ = PriorityQueue()
for _ in range(N):
    x = int(input())
    if x == 0:
        if PQ.empty():
            print(0)
        else:
            print(-PQ.get())
    else:
        PQ.put(-x)