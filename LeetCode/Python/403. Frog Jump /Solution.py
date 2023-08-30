from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0] = {0}

        for stone in stones:
            for jump in dp[stone]:
                for jump_distance in [jump - 1, jump, jump + 1]:
                    if 0 < jump_distance and stone + jump_distance in dp:
                        dp[stone + jump_distance].add(jump_distance)

                    print(stone, jump, jump_distance, dp)

        return dp[stones[-1]]


if __name__ == "__main__":
    stones = [0,1,3,5,6,8,12,17]
    ans = True
    print(Solution().canCross(stones))
