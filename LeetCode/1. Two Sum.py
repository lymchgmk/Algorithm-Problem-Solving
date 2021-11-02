from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, n1 in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if i1 != i2 and n1 + n2 == target:
                    return [i1, i2]




