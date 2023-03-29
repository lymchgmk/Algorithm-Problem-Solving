def solution(wallpaper):
    MAX_X, MAX_Y = len(wallpaper), len(wallpaper[0])
    lux, luy, rux, ruy = (MAX_X, MAX_Y, 0, 0)

    for x in range(MAX_X):
        for y in range(MAX_Y):
            if wallpaper[x][y] == '#':
                lux = min(lux, x)
                luy = min(luy, y)
                rux = max(rux, x)
                ruy = max(ruy, y)

    return [lux, luy, rux + 1, ruy + 1]


if __name__ == "__main__" :
    wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
    result = [1, 3, 5, 8]
    print(solution(wallpaper))