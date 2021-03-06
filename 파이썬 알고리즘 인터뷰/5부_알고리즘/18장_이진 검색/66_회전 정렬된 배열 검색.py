from typing import List


# 풀이 1. 피벗을 기준으로 한 이진 탐색
def search(self, nums: List[int], target: int) -> int:
    # 예외처리
    if not nums:
        return -1
    
    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    pivot = left
    
    # 피벗 기준 탐색
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)
        
        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    
    return -1