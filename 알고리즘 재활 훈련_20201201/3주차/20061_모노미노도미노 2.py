import sys
sys.stdin = open('20061_모노미노도미노 2.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


def get_point():
    def blue_point(blue_board):
        L = len(blue_board)
        point = 0
        while True:
            for i in range(L-1, 1, -1):
                col = [row[i] for row in blue_board]
                if sum(col) == 4:
                    point += 1
                    break
            for i in range(L-1, 1, -1):
                

    pass
        


def cut_board():
    pass



N = int(input())

blue_board = [[0]*6 for _ in range(4)]
green_board = [[0]*4 for _ in range(6)]

row = [row for row in blue_board]
col = [row[i] for i in range(len())]

point = 0
for _ in range(N):
    red_board = [[0]*4 for _ in range(4)]
    t, x, y = map(int, input())

