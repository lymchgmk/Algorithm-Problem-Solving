from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))

        prev = pairs[0]
        res = 1

        for curr in pairs[1:]:
            if curr[0] > prev[1]:
                res += 1
                prev = curr

        return res
