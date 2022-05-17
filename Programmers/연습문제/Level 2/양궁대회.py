from itertools import combinations_with_replacement
from collections import Counter


def solution(n, info):
    def calc_points(apeach, ryan):
        _points = {"apeach": 0, "ryan": 0}
        for k in range(11):
            if apeach[k] == 0 and ryan[k] == 0:
                continue

            if apeach[k] >= ryan[k]:
                _points["apeach"] += k
            elif apeach[k] < ryan[k]:
                _points["ryan"] += k
        return _points

    def cntr2lst(cntr):
        res = [0]*11
        for key in cntr:
            res[10-key] = cntr[key]
        return res

    apeach = Counter()
    for idx, val in enumerate(info):
        apeach[10-idx] += val

    max_diff_point = 0
    cands = None
    for comb in combinations_with_replacement(range(0, 11), n):
        ryan = Counter(comb)
        points = calc_points(apeach, ryan)
        diff_point = points["ryan"] - points["apeach"]
        if diff_point > 0 and max_diff_point < diff_point:
            max_diff_point = diff_point
            cands = ryan
    return cntr2lst(cands) if cands else [-1]


if __name__ == "__main__":
    n = 9
    info = [0,0,1,2,0,1,1,1,1,1,1]
    print(solution(n, info))

    # n = 10
    # info = [0,0,0,0,0,0,0,0,3,4,3]
    # print(solution(n, info))