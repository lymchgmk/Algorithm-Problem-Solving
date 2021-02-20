# 풀이 1. 리스트로 변환
def isPalindrome_1(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True


# 풀이 2. 데크 자료형을 이용한 최적화
import collections


def isPalindrome_2(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
        
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
