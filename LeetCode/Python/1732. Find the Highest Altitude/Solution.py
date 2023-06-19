import sys
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = 0
        currAlti = 0
        for height in gain:
            currAlti += height
            answer = max(answer, currAlti)

        return answer


if __name__ == "__main__":
    gain = [-4,-3,-2,-1,4,3,2]
    output = 0
    answer = Solution().largestAltitude(gain)
    print(answer == output, answer)