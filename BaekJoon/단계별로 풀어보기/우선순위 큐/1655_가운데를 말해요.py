import sys
sys.stdin = open("1655_가운데를 말해요.txt", "rt")
input = lambda: sys.stdin.readline().strip()
import heapq


N = int(input())
min_heap, max_heap = [], []
for _ in range(N):
    n = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(min_heap, (-n, n))
    else:
        heapq.heappush(max_heap, (n, n))
    
    if max_heap and min_heap[0][1] > max_heap[0][1]:
        min_heap_n = heapq.heappop(min_heap)[1]
        max_heap_n = heapq.heappop(max_heap)[1]
        heapq.heappush(max_heap, (min_heap_n, min_heap_n))
        heapq.heappush(min_heap, (-max_heap_n, max_heap_n))
    
    print(min_heap[0][1])