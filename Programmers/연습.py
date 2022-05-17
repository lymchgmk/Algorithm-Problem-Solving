def points(apeach, ryan):
    a, r = 0, 0
    for i in range(11):
        if apeach[i] == ryan[i] == 0:
            continue
        else:
            if apeach[i] >= ryan[i]:
                a += 10 - i
            else:
                r += 10 - i
    return a, r


def solution(n, info):
    stuff = [[0, 0, -1]]
    for i in range(11):
        if info[i]:
            stuff.append([10-i, info[i] + 1, 2*(10-i)])
        else:
            stuff.append([10-i, info[i] + 1, 10 - i])
    stuff.sort(key=lambda x: (x[1], -x[2], x[0]))

    knapsack = [[[0, []] for _ in range(n + 1)] for _ in range(12)]
    for i in range(1, 12):
        for j in range(1, n+1):
            target_num, weight, value = stuff[i]
            if j < weight:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                if value + knapsack[i - 1][j - weight][0] <= knapsack[i - 1][j][0]:
                    knapsack[i][j] = knapsack[i - 1][j]
                else:
                    knapsack[i][j][0] = value + knapsack[i - 1][j - weight][0]
                    knapsack[i][j][1] = knapsack[i - 1][j - weight][1] + [target_num]*weight

    ryan = [0]*11
    for i in knapsack[-1][-1][-1]:
        ryan[10-i] += 1

    apeach_points, ryan_points = points(info, ryan)
    if apeach_points >= ryan_points:
        return [-1]
    else:
        ryan[10] += n - sum(ryan)
        return ryan



n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))

# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]
# print(solution(n, info))