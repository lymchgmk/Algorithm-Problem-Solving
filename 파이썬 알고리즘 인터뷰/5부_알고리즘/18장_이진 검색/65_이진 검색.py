from typing import List
import bisect


# 풀이 1. 재귀 풀이
def search_1(self, nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2
            '''
            파이썬은 임의 정밀도 정수형을 지원하기 때문에 left + right 가 오버플로우 발생하지 않지만, 자료형이 엄격한 언어들의 경우에 문제가 발생할 수 있음.
            mid = left + (right - left) // 2
            '''
            
            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1
    
    return binary_search(0, len(nums)-1)


# 풀이 2. 반복 풀이
def search_2(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
        
    return -1


# 풀이 3. 이진 검색 모듈
def search_3(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    
    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1
    

# 풀이 4. 이진 검색을 사용하지 않는 index 풀이
def search_4(self, nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1