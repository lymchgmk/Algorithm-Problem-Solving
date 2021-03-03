import collections


# 풀이 1. 재귀 구조 브루트 포스
def climbStairs_1(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs_1(n-1) + self.climbStairs_1(n-2)


# 풀이 2. 메모메이제이션
class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs_2(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs_2(n - 1) + self.climbStairs_2(n - 2)
        return self.dp[n]
