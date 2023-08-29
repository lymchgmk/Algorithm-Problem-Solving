from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = [[nums1[0], nums2[0]]]
        idx1, idx2 = 0, 0

        for _ in range(k - 1):
            if idx1 == len(nums1) - 1 and idx2 == len(nums2) - 1:
                break

            post_idx1 = min(idx1 + 1, len(nums1) - 1)
            post_idx2 = min(idx2 + 1, len(nums2) - 1)
            if


            cand1 = [nums1[idx1], nums2[idx2 + 1]]
            cand2 = [nums1[idx1 + 1], nums2[idx2]]

            if sum(cand1) < sum(cand2):
                idx2 += 1
                pairs.append(cand1)
            else:
                idx1 += 1
                pairs.append(cand2)

        return pairs

if __name__ == "__main__":
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    answer = [[1, 2], [1, 4], [1, 6]]
    result = Solution().kSmallestPairs(nums1, nums2, k)
    print(answer == result, result)
