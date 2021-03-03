from typing import List
import collections


# 풀이 1. 브루트 포스로 과반수 비교
def majorityElement_1(self, nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num


# 풀이 2. 다이나믹 프로그래밍
def majorityElement_2(self, nums: List[int]) -> int:
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
    
        if counts[num] > len(nums) // 2:
            return num
        

# 풀이 3. 분할 정복
def majorityElement_3(self, nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    a = self.majorityElement(nums[:half])
    b = self.majorityElement(nums[half:])
    
    return [b, a][nums.count(a) > half]