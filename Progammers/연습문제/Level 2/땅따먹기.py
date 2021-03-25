def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max([val for idx, val in enumerate(land[i-1]) if idx != j])

    return max(land[-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))