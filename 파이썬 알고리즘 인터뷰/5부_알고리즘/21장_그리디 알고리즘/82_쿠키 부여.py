from typing import List
import bisect


# 풀이 1. 그리디 알고리즘
def findContentChildren_1(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    
    child_i = cookie_j = 0
    # 만족하지 못할 때까지 그리디 진행
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
        
    return child_i


# 풀이 2. 이진 탐색
def findContentChildren_2(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    
    result = 0
    for i in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    
    return result
