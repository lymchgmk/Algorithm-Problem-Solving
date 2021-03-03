from typing import List
import sys


# 풀이 1. 메모이제이션
def maxSubArray_1(self, nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)


# 풀이 2. 카데인 알고리즘
def maxSubArray_2(self, nums: List[int]) -> int:
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
        
    return best_sum
