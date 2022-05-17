from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            for order_comb in combinations(order, k):
                candidates.append(''.join(sorted(order_comb)))
        
        menu_Counter = Counter(candidates).most_common()
        answer += [menu for menu, cnt in menu_Counter if cnt >= 2 and cnt == menu_Counter[0][1]]
    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))