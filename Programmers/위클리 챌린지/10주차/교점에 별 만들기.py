from itertools import combinations


def make_point(l1, l2):
    A, B, E = l1
    C, D, F = l2
    if A*D - B*C != 0:
        p, r = divmod((B*F - E*D), (A*D - B*C))
        q, s = divmod((E*C - A*F), (A*D - B*C))
        if r == 0 and s == 0:
            return p, -q


def solution(line):
    points = []
    INF = float('inf')
    r_min, r_max, c_min, c_max = INF, -INF, INF, -INF
    for l1, l2 in combinations(line, 2):
        point = make_point(l1, l2)
        if point:
            c, r = point
            r_min = min(r_min, r)
            r_max = max(r_max, r)
            c_min = min(c_min, c)
            c_max = max(c_max, c)
            points.append(point)

    answer = [['.'] * (c_max - c_min + 1) for _ in range(r_max - r_min + 1)]
    for c, r in points:
        answer[r - r_min][c - c_min] = '*'
    return [''.join(a) for a in answer]


if __name__ == "__main__":
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    print(solution(line))

    line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
    print(solution(line))

    line = [[1, -1, 0], [2, -1, 0]]
    print(solution(line))

    line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
    print(solution(line))
