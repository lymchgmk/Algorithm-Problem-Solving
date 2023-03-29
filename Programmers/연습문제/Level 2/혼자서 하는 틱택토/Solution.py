from collections import defaultdict


def solution(board):
    counts = defaultdict(int)

    for r in range(len(board)):
        for c in range(len(board[0])):
            grid = board[r][c]
            counts[grid] += 1

    if counts["O"] == 0 and counts["X"] == 0:
        return 1

    if not (counts["O"] == counts["X"] or counts["O"] == counts["X"] + 1):
        return 0

    first_is_winner = second_is_winner = False

    for row in board:
        if all(grid == "O" for grid in row):
            first_is_winner = True
        if all(grid == "X" for grid in row):
            second_is_winner = True

    for col in zip(*board):
        if all(grid == "O" for grid in col):
            first_is_winner = True
        if all(grid == "X" for grid in col):
            second_is_winner = True

    diagonal = [board[r][c] for r in range(len(board)) for c in range(len(board[0])) if r == c]
    if all(grid == "O" for grid in diagonal):
        first_is_winner = True
    if all(grid == "X" for grid in diagonal):
        second_is_winner = True

    rev_diagonal = [board[r][c] for r in range(len(board)) for c in range(len(board[0])) if r + c + 1 == len(board)]
    if all(grid == "O" for grid in rev_diagonal):
        first_is_winner = True
    if all(grid == "X" for grid in rev_diagonal):
        second_is_winner = True

    if first_is_winner and second_is_winner:
        return 0
    else:
        if first_is_winner and not second_is_winner and counts["O"] == counts["X"]:
            return 0
        elif not first_is_winner and second_is_winner and counts["O"] == counts["X"] + 1:
            return 0

    return 1


if __name__ == "__main__":
    board = ["O.X", ".O.", "..X"]
    result = 1
    answer = solution(board)
    print(f'[{answer == result}] {answer}')
