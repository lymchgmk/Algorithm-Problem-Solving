import sys
sys.stdin = open("19235_모노미노도미노.txt", "r")

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

red = [[0] * 4 for _ in range(4)]
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]

def blue_tetris(block, blue):
    t, x, y = block[0], block[1], block[2]

    if t == 1:
        for i in range(5, -1, -1):
            blue_col = [row[i] for row in blue]
            if blue_col.count(0) == 4:
                blue[x][]

    elif t == 2:
        pass

    elif t == 3:
        pass


def green_tetris(block, green):
    t, x, y = block[0], block[1], block[2]

    if t == 1:
        for i in range(5, -1, -1):
            green_row = green[i]
            if green_row.count(0) == 4:
                blue[x][]

    elif t == 2:
        pass

    elif t == 3:
        pass

def light_blue_push():
    pass

def light_green_push():
    pass

for block in data:
    print(blue_tetris(block, blue))