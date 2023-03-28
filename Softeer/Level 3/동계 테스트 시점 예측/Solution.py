import sys


def find_ices():
    ices = []
    for r in range(N):
        for c in range(M):
            if grids[r][c]:
                ices.append((r, c))
    return ices


def melt(ices):
    global grids

    melted = []
    for ice_r, ice_c in ices:
        no_ices = 0
        for dir_r, dir_c in dirs:
            check_r, check_c = ice_r + dir_r, ice_c + dir_c
            if not grids[check_r][check_c]:
                no_ices += 1

        if no_ices >= 2:
            melted.append((ice_r, ice_c))

    for melt_r, melt_c in melted:
        grids[melt_r][melt_c] = 0


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N, M = map(int, input().split())
    grids = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    time = 0
    while True:
        ices = find_ices()
        if not ices:
            break

        melt(ices)
        time += 1

    print(time)
