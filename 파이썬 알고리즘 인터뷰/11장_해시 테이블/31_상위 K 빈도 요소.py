import collections
from typing import List
import heapq


# 풀이 1. Counter를 이용한 음수 순 추출
def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    
    topk = list()
    # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
        
    return topk


# 풀이 2. 파이썬다운 방식
def topKFrequent_2(self, nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]