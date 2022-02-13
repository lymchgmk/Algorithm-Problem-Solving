import sys
from itertools import combinations
sys.stdin = open("15686_치킨 배달.txt", "rt")


def solution(N, M, city):
    houses, chickens = [], []
    for r in range(N):
        for c in range(N):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chickens.append((r, c))

    answer = float('inf')
    for comb in combinations(chickens, M):
        total_dist = 0
        for house_r, house_c in houses:
            min_dist = float('inf')
            for chicken_r, chicken_c in comb:
                min_dist = min(min_dist, abs(house_r - chicken_r) + abs(house_c - chicken_c))
            total_dist += min_dist
        answer = min(answer, total_dist)
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, city))