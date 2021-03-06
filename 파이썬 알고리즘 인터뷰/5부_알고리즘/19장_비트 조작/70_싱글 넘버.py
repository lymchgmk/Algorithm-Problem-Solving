from typing import List


# 풀이 1. XOR 풀이
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    
    return result
