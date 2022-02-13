import sys
from copy import deepcopy
from collections import deque, defaultdict
sys.stdin = open('13460_구슬 탈출 2.txt', 'rt')


def solution(N, M, board):
    def find_RBO(board):
        RBO = {}
        for r in range(N):
            for c in range(M):
                if board[r][c] in ('R', 'B', 'O'):
                    RBO[board[r][c]] = (r, c)
        return RBO

    def RB_move_priority(dir, R, B):
        return sorted([R, B], key=lambda x: (-dir[0] * x[0], -dir[1] * x[1]))

    def move(curr_board, dir):
        post_board = deepcopy(curr_board)
        RBO = find_RBO(post_board)
        first, second = RB_move_priority(dir, RBO['R'], RBO['B'])
        # dir 방향에 RB가 둘 다 있는 경우
        check_r, check_c = RBO['O']
        is_answer = False
        while 0 <= check_r + dir[0] < N and 0 <= check_c + dir[1] < M:
            check_r, check_c = check_r + dir[0], check_c + dir[1]
            if post_board[check_r][check_c] == 'R':
                is_answer = True
            elif post_board[check_r][check_c] in ('B', '#'):
                is_answer = False
        if not

        can_move = [True, True]
        while can_move[0] or can_move[1]:
            can_move[0] = post_board[first[0] + dir[0]][first[1] + dir[1]] == '.'
            if can_move[0]:
                post_board[first[0]][first[1]], post_board[first[0] + dir[0]][first[1] + dir[1]] = \
                    post_board[first[0] + dir[0]][first[1] + dir[1]], post_board[first[0]][first[1]]
                first = [first[0] + dir[0], first[1] + dir[1]]

            can_move[1] = post_board[second[0] + dir[0]][second[1] + dir[1]] == '.'
            if can_move[1]:
                post_board[second[0]][second[1]], post_board[second[0] + dir[0]][second[1] + dir[1]] = \
                    post_board[second[0] + dir[0]][second[1] + dir[1]], post_board[second[0]][second[1]]
                second = [second[0] + dir[0], second[1] + dir[1]]

        return post_board, is_answer

    def board2str(curr_board):
        res = ""
        for cb in curr_board:
            res += ''.join(cb)
        return res

    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    dq = deque([[board, 0]])
    check = defaultdict(lambda: False)
    check[board2str(board)] = True
    while dq:
        curr_board, curr_cnt = dq.popleft()
        for dir in dirs:
            post_board, is_answer = move(curr_board, dir)
            post_cnt = curr_cnt + 1
            print("before")
            for b in curr_board:
                print(b)
            print()

            print(post_cnt, dir, is_answer)
            for b in post_board:
                print(b)
            print()
            if post_cnt >= 10:
                return -1

            if is_answer:
                return post_cnt
            else:
                if not check[board2str(post_board)]:
                    check[board2str(post_board)] = True
                    dq.append([post_board,  post_cnt])
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print(solution(N, M, board))
