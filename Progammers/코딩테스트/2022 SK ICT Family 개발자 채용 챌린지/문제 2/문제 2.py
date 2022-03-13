def solution(n, clockwise):
    def insert_nums(points, target):
        nonlocal arr
        for point in points:
            _dir_idx, _pos = point
            x, y = _pos
            if arr[x][y] == 0:
                arr[x][y] = target

    def move_points(points, clockwise):
        moved_points = []
        for point in points:
            _dir_idx, _pos = point
            x, y = _pos
            dx, dy = dirs[clockwise][_dir_idx]
            if arr[x + dx][y + dy] != 0:
                _dir_idx = (_dir_idx + 1) % 4
            dx, dy = dirs[clockwise][_dir_idx]
            moved_points.append((_dir_idx, [x + dx, y + dy]))
        return moved_points

    dirs = {True: ((0, 1), (1, 0), (0, -1), (-1, 0)),
            False: ((1, 0), (0, 1), (-1, 0), (0, -1))}
    poses = {True: ([0, 0], [0, n-1], [n-1, n-1], [n-1, 0]),
            False: ([0, 0], [n-1, 0], [n-1, n-1], [0, n-1])}
    points = list(zip([0, 1, 2, 3], poses[clockwise]))

    arr = [[0] * n for _ in range(n)]
    cnt = (n**2 - 1) // 4
    for i in range(1, cnt+2):
        insert_nums(points, i)
        points = move_points(points, clockwise)
    return arr


if __name__ == "__main__":
    # tc 1
    n = 5
    clockwise = True
    print(solution(n, clockwise))

    # tc 2
    n = 6
    clockwise = False
    print(solution(n, clockwise))

    # tc 3
    n = 9
    clockwise = False
    print(solution(n, clockwise))