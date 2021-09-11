from collections import defaultdict


def _points(versus, shoot):
    return sum(10 - i for i in range(11) if versus[i] < shoot[i])


def solution(n, info):
    cost = [[0, 0]]*11
    for i in range(11):
        if info[i]:
            cost[i] = [2*(10-i), info[i]+1, i]
        else:
            cost[i] = [10 - i, info[i] + 1, i]
    cost.sort(key=lambda x: x[0] / x[1], reverse=True)

    ryan = [0]*11
    arrows_cnt = 0
    while arrows_cnt != n:
        for point, arrows, idx in cost:
            print(point, arrows, idx)





n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))

# n, info = 9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
# print(solution(n, info)) # [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]