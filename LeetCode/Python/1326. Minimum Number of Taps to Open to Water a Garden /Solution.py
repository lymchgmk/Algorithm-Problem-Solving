from typing import List


class Solution:
    INF = float('inf')

    def minTapsGreedy(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n + 1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue

            left = max(0, i - r)
            arr[left] = max(arr[left], i + r)

        end, far_can_reach, cnt = 0, 0, 0

        for i, reach in enumerate(arr):
            if end < i:
                if far_can_reach <= end:
                    return -1
                end, cnt = far_can_reach, cnt + 1
            far_can_reach = max(far_can_reach, reach)

        return cnt + (end < n)

    def minTapsDP(self, n: int, ranges: List[int]) -> int:
        dp = [Solution.INF] * (n + 1)
        dp[0] = 0

        for i, r in enumerate(ranges):
            start, end = max(0, i - r), min(n, i + r)
            for j in range(start, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)

            print(i, r, dp)

        return dp[-1] if dp[-1] != Solution.INF else -1


if __name__ == "__main__":
    n = 5
    ranges = [3,4,1,1,0,0]
    ans = 1
    print(Solution().minTapsDP(n, ranges))
