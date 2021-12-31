import sys
sys.stdin = open("11286_절댓값 힙.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


N = int(input())
abs_heap = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(abs_heap, [abs(x), x])
    else:
        if not abs_heap:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])