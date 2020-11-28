import sys
sys.stdin = open("1927_최소 힙.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


N = int(input())
min_heap = []
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))

    else:
        heapq.heappush(min_heap, tmp)