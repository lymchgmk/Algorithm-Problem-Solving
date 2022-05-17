from collections import defaultdict
from math import comb
from functools import lru_cache


@lru_cache(maxsize=None)
def comb_cache(n, k):
    return comb(n, k)


def solution(a):
    a_cols = list(zip(*a))
    one_cnt = [sum(ones) for ones in zip(*a)]  # 각열 1의 갯수

    # DP = defaultdict(int,{(rows := len(a))-one_cnt[0]:comb(rows, one_cnt[0])}) # 1열까지 계산한 DP
    DP = [[0] * (N := len(a[0])) for _ in range(len(a))]
    return DP

    # for ones in one_cnt[1:]: # DP[2][j] 부터 계산
    #     next_DP = defaultdict(int)
    #     for even_rows in DP:
    #         odd_rows = rows-even_rows
    #         for add_one in range(max(0,ones-odd_rows), min(ones,even_rows)+1): # range 범위는 미만이기때문에 +1
    #             next_DP[even_rows+ones-2*add_one] += DP[even_rows] * C(even_rows, add_one) * C(odd_rows, ones-add_one)%(10**7+19)
    #     DP = next_DP
    # return DP[rows]


if __name__ == "__main__":
    a = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(list(zip(*a)))
    print(solution(a))
