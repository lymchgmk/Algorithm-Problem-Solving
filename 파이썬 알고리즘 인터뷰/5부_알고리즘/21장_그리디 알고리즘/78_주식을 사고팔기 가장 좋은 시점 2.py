from typing import List


# 풀이 1. 그리디 알고리즘
def maxProfit_1(self, prices: List[int]) -> int:
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result


# 풀이 2. 파이썬다운 방식
def maxProfit_2(self, prices: List[int]) -> int:
    # 0보다 크면 무조건 합산
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
