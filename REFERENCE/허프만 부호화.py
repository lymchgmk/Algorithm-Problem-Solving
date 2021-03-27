from heapq import heappush, heappop, heapify
from collections import defaultdict

def HUFF(symb2freq):
    heap = [[wt, [sym, '']] for sym, wt in symb2freq.items()]
    heapify(heap)
    while heap:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: [len(p[-1]), p])