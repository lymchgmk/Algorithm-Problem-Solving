from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return list(map(lambda x: bin(x).count('1'), range(n)))


if __name__ == "__main__":
    n = 5
    ans = [0,1,1,2,1,2]
    print(Solution().countBits(n))

