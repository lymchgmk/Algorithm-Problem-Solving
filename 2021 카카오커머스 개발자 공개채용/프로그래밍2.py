from itertools import combinations


def solution(grid, K):
    L = len(grid)
    _sum = []
    for start_x in range(L-K+1):
        for start_y in range(L-K+1):
            cafe_sum = 0
            for cafe_x in range(K):
                for cafe_y in range(K):
                    cafe_sum += grid[start_x + cafe_x][start_y + cafe_y]
            _sum.append([[start_x, start_y], cafe_sum])
    
    answer = float('-inf')
    for s in combinations(_sum, 2):
        cafe1, cafe2 = s
        p1, sum1 = cafe1
        p2, sum2 = cafe2
        if not (p1[0] <= p2[0] < p1[0]+K and p1[1] <= p2[1] < p1[1]+K):
             answer = max(answer, sum1+sum2)
    return answer


grid = [[2, 1, 1, 0, 1], [1, 2, 0, 3, 0], [0, 1, 5, 1, 2], [0, 0, 1, 3, 1], [1, 2, 0, 1, 1]]
K = 2
print(solution(grid, K))
