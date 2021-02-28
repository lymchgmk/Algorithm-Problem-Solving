from typing import List
import heapq


# 풀이 1. heapq 모듈 이용
def findKthLargest_1(self, nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
        
    for _ in range(k):
        heapq.heappop(heap)
        
    return -heapq.heappop(heap)


# 풀이 2. heapq 모듈의 heapify 이용
def findKthLargest(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
        
    return heapq.heappop(nums)


# 풀이 3. heapq 모듈의 nlargest 이용
def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


# 풀이 4. 정렬을 이용한 풀이
def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]
