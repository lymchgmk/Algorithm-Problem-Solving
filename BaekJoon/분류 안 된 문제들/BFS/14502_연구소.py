import sys
from itertools import combinations
from copy import deepcopy
sys.stdin = open("14502_연구소.txt", 'rt')


def solution(N, M, arr):
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def find_virus_sources():
        return [(r, c) for r in range(N) for c in range(M) if arr[r][c] == 2]

    def find_wall_cands():
        return [(r, c) for r in range(N) for c in range(M) if arr[r][c] == 0]

    def install_3_walls(walls):
        _res = deepcopy(arr)
        for wall_r, wall_c in walls:
            _res[wall_r][wall_c] = 1
        return _res

    def spread_virus(_arr, virus_sources):
        for virus in virus_sources:
            stack = [virus]
            while stack:
                virus_r, virus_c = stack.pop()
                for dr, dc in dirs:
                    if 0 <= virus_r + dr < N and 0 <= virus_c + dc < M and _arr[virus_r + dr][virus_c + dc] == 0:
                        _arr[virus_r + dr][virus_c + dc] = 2
                        stack.append((virus_r + dr, virus_c + dc))
        return _arr

    def count_safe_zone(arr):
        return sum([True for r in range(N) for c in range(M) if arr[r][c] == 0])

    virus_sources = find_virus_sources()
    wall_cands = find_wall_cands()
    answer = 0
    for wall_cand in combinations(wall_cands, 3):
        _arr = install_3_walls(wall_cand)
        _arr = spread_virus(_arr, virus_sources)
        answer = max(answer, count_safe_zone(_arr))
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, arr))
