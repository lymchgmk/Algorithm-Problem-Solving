from itertools import combinations


def make_point(l1, l2):
    A, B, E = map(float, l1)
    C, D, F = map(float, l2)
    if A*D - B*C != 0:
        x = (B*F - E*D) / (A*D - B*C)
        y = (E*C - A*F) / (A*D - B*C)
        if x == int(x) and y == int(y):
            return int(x), int(y)

def draw_stars(points):
    Y, X = map(list, zip(*points))
    Y.sort()
    X.sort()
    Y_min, Y_max = Y[0], Y[-1]
    X_min, X_max = X[0], X[-1]
    res = [['.']*(Y_max - Y_min + 1) for _ in range(X_max - X_min + 1)]
    zp_y, zp_x = (Y_max - Y_min) // 2, (X_max - X_min) // 2
    for py, px in points:
        res[zp_x - px][zp_y + py] = '*'

    return [''.join(r) for r in res]


def solution(line):
    points = []
    for l1, l2 in combinations(line, 2):
        point = make_point(l1, l2)
        if point:
            points.append(point)
    return draw_stars(points)


if __name__ == "__main__":
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    print(solution(line))

    line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
    print(solution(line))

    line = [[1, -1, 0], [2, -1, 0]]
    print(solution(line))

    line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
    print(solution(line))