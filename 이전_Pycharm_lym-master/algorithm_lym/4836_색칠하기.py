import sys
sys.stdin = open("4836_색칠하기.txt", "r")


def color_area(color, grid):
    for i in range(len(color)):
        if color[i][-1] == 1:
            for x in range(color[i][0], color[i][2]+1):
                for y in range(color[i][1], color[i][3]+1):
                    grid[x][y] += 1

        elif color[i][-1] == 2:
            for x in range(color[i][0], color[i][2]+1):
                for y in range(color[i][1], color[i][3]+1):
                    grid[x][y] += 2

    return grid

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0]*10 for _ in range(10)]
    color = []

    for idx in range(N):
        color.append(list(map(int, input().split())))

    color_area(color, grid)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 3:
                count += 1

    print("#{0} {1}".format(test_case, count))