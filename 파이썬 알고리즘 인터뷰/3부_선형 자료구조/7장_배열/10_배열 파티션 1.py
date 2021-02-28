from typing import List


# 풀이 1. 오름차순 풀이
def arrayPairSum_1(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
        
    return sum


# 풀이 2. 짝수 번쨰 값 계산
def arrayPairSum_2(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()
    
    for i, n in enumerate(nums):
        # 짝수 번쨰 값의 합 계산
        if i%2 == 0:
            sum += n
            
    return sum


# 풀이 3. 파이썬다운 방식
def arrayPairSum_3(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
