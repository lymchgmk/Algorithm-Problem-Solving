from itertools import permutations


def solution(board, r, c):
    cards = set([board[i][j] for i in range(4) for j in range(4)])
    cards.remove(0)
    card_ranks = permutations(cards, len(cards))
    for card_rank in card_ranks:
        pass


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board, r, c))
# 14

# board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
# r = 0
# c = 1
# print(solution(board, r, c))
# # 16