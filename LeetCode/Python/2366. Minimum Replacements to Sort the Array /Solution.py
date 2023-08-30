from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replace_count = 0
        upper_bound = nums[-1]

        for num in reversed(nums[:-1]):
            divided_count = (num + (upper_bound - 1)) // upper_bound
            replace_count += divided_count - 1
            upper_bound = num // divided_count

        return replace_count


if __name__ == "__main__":
    nums = [12,9,7,6,17,19,21]
    ans = 6
    solution = Solution()
    print(solution.minimumReplacement(nums))
