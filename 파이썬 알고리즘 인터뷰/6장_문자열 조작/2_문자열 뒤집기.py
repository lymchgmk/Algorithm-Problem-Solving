# 풀이 1. 투 포인터를 이용한 스왑
def reverseString_1(self, s: list) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


def reverseString_2(self, s: list) -> None:
    s.reverse()
    return s
