from collections import deque, defaultdict
from itertools import permutations


def solution(board, r, c):
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    def check_distance(board, cursor, target_card):
        deq = deque([[cursor, 0]])
        while deq:
            cursor, cnt = deq.popleft()
            curr_x, curr_y = cursor
            if board[curr_x][curr_y] == target_card:
                return [curr_x, curr_y], cnt
            
            for dir_x, dir_y in dirs:
                post_x, post_y = curr_x + dir_x, curr_y + dir_y
                if 0<=post_x<4 and 0<=post_y<4:
                    deq.append([[post_x, post_y], cnt+1])
            
            for dir_x, dir_y in dirs:
                post_x, post_y = curr_x + dir_x, curr_y + dir_y
                while 0<=post_x<4 and 0<=post_y<4 and board[post_x][post_y] == 0:
                    post_x += dir_x
                    post_y += dir_y
                deq.append([[post_x, post_y], cnt + 1])
                
        return -1
    
    cards = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards[board[i][j]].append([i, j])
    print(cards)
    
    for order in permutations(cards.keys(), len(cards.keys())):
        cursor = [r, c]
        tmp = 0
        for target_card in order:
            print(cursor)
            cursor, cnt = check_distance(board, cursor, target_card)
            print(cursor, cnt)
            tmp += cnt
            board[cursor[0]][cursor[1]] = 0
        print(tmp)
        

if __name__ == "__main__":
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