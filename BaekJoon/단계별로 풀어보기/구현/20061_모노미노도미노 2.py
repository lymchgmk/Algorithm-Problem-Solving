import sys
sys.stdin = open("20061_모노미노도미노 2.txt", "rt")


class BlueBoard:
    def __init__(self):
        self.board = [[0]*6 for _ in range(4)]
        self.point = 0

    def stack_block(self):
        pass

    def add_point(self):
        pass

    def cut_off(self):
        pass

    def count_block(self):
        _res = 0
        for r in range(4):
            for c in range(6):
                if self.board[r][c] != 0:
                    _res += 1
        return _res


class GreenBoard:
    def __init__(self):
        self.board = [[0]*4 for _ in range(6)]
        self.point = 0

    def stack_block(self):
        pass

    def add_point(self):
        pass

    def cut_off(self):
        pass

    def count_block(self):
        _res = 0
        for r in range(6):
            for c in range(4):
                if self.board[r][c] != 0:
                    _res += 1
        return _res


def solution(t, r, c):
    global blue_board, green_board

    blue_board.stack_block()
    green_board.stack_block()

    blue_board.add_point()
    green_board.add_point()

    blue_board.cut_off()
    green_board.cut_off()


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    blue_board = BlueBoard()
    green_board = GreenBoard()
    for _ in range(N):
        t, r, c = map(int, input().split())
        solution(t, r, c)
