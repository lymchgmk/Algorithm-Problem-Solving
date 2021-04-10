from itertools import permutations, product


def solution(board, r, c):
    # 카드 한 종류를 (삭제 후의 보드, 커서 위치, 누른 버튼의 총 수)를 리턴해주는 함수를 구현하자 (2개의 답이 나올것)
    def find_and_flip():
        return (board, cursor, cnt)
    # 카드를 다 삭제하면 return
    
    # 카드 우선순위 정하기
    cards = set([board[i][j] for i in range(4) for j in range(4)])
    cards.remove(0)
    card_ranks = permutations(cards, len(cards))
    answer = float('inf')
    # 우선순위에 따라 카드 삭제
    for card_rank in card_ranks:
        before = [[board, [r, c]]]
        after = []
        # 버튼 횟수 측정
        for target in card_rank:
            while before:
                after.append(find_and_flip())
            before, after = after, []
        
        for _, _, cnt in before:
            answer = min(answer, cnt)
    
    return answer
    


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