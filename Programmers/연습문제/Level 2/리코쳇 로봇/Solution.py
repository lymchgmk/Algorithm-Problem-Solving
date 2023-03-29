from collections import deque


dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solution(board):
    MAX_R, MAX_C = len(board), len(board[0])

    start, end = (0, 0), (0, 0)
    for r in range(MAX_R):
        for c in range(MAX_C):
            if board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                end = (r, c)

    dq = deque([(start[0], start[1], 0)])
    counts = [[float('inf')] * MAX_C for _ in range(MAX_R)]

    while dq:
        if counts[end[0]][end[1]] not in (0, float("inf")) :
            return counts[end[0]][end[1]]

        curr_r, curr_c, curr_count = dq.popleft()
        counts[curr_r][curr_c] = curr_count

        for dir_r, dir_c in dirs:
            post_r, post_c, post_count = curr_r, curr_c, curr_count + 1

            while 0 <= post_r + dir_r < MAX_R and 0 <= post_c + dir_c < MAX_C and board[post_r + dir_r][post_c + dir_c] != 'D':
                post_r += dir_r
                post_c += dir_c

            if post_count < counts[post_r][post_c]:
                counts[post_r][post_c] = post_count
                dq.append((post_r, post_c, post_count))

    return -1


if __name__ == "__main__":
    board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
    result = 7
    print(solution(board))
    print(solution(board) == result)
