import sys
from collections import deque
sys.stdin = open("16236_아기 상어.txt", "rt")


class Shark:
    def __init__(self, pos_r, pos_c):
        self.pos_r, self.pos_c = pos_r, pos_c
        self.size = 2
        self.grow_cnt = 0
        self.call_mom_time = 0

    def getPos(self):
        return (self.pos_r, self.pos_c)

    def setPos(self, pos):
        self.pos_r, self.pos_c = pos[0], pos[1]

    def eat(self, fish_time):
        self.call_mom_time += fish_time
        self.grow_cnt += 1

    def grow(self):
        if self.grow_cnt == self.size:
            self.grow_cnt = 0
            self.size += 1


def solution(N, board):
    def find_shark(board):
        for r in range(N):
            for c in range(N):
                if board[r][c] == 9:
                    board[r][c] = 0
                    return Shark(r, c)

    def find_fish(board):
        nonlocal shark
        shark_pos = shark.getPos()
        min_time = float('inf')
        times = [[-1]*N for _ in range(N)]
        times[shark_pos[0]][shark_pos[1]] = 0
        dirs = ((-1, 0), (0, -1), (0, 1), (1, 0))
        dq = deque([shark_pos])
        edible = []
        while dq:
            curr_r, curr_c = dq.popleft()
            if min_time < times[curr_r][curr_c]:
                break
            for d_r, d_c in dirs:
                post_r, post_c = curr_r + d_r, curr_c + d_c
                if 0 <= post_r < N and 0 <= post_c < N and times[post_r][post_c] == -1:
                    if shark.size < board[post_r][post_c]:
                        continue
                    elif 0 < board[post_r][post_c] < shark.size:
                        times[post_r][post_c] = times[curr_r][curr_c] + 1
                        if times[post_r][post_c] <= min_time:
                            edible.append((times[post_r][post_c], (post_r, post_c)))
                            min_time = times[post_r][post_c]
                    else:
                        times[post_r][post_c] = times[curr_r][curr_c] + 1
                        dq.append((post_r, post_c))
        edible.sort()
        _fish = edible[0] if edible else []
        return _fish

    shark = find_shark(board)
    while True:
        res = find_fish(board)
        if not res:
            break
        else:
            time, fish = res
        shark.eat(time)
        board[fish[0]][fish[1]] = 0
        shark.grow()
        shark.setPos(fish)
    print(shark.call_mom_time)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    solution(N, board)
