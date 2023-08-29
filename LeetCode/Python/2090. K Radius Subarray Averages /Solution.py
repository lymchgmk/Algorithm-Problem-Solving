from typing import List
from collections import deque


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        window_size = 2 * k + 1
        window = deque()
        result = [-1] * len(nums)
        MIN_IDX, MAX_IDX = 0, len(nums) - 1

        for i in range(k, len(nums) - k):
            print(i)

        return result


if __name__ == "__main__":
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    output = [-1,-1,-1,5,4,4,-1,-1,-1]
    answer = Solution().getAverages(nums, k)
    print(answer == output, answer)
