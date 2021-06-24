def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
        
    block_pang = []
    while True:
        for x in range(m):
            for y in range(n):
                check = board[x][y]
                for i in range(2):
                    for j in range(2):
                        if not (check != False and 0<=x+i<m and 0<=y+j<n and board[x+i][y+j] == check):
                            break
                    else:
                        continue
                    break
                else:
                    for i in range(2):
                        for j in range(2):
                            block_pang.append((x+i, y+j))

        if not block_pang:
            break

        else:
            block_pang = list(set(block_pang))
            answer += len(block_pang)

            for bp in block_pang:
                board[bp[0]][bp[1]] = False
            
            new_col = []
            for i in range(n):
                col = [row[i] for row in board]
                false_cnt = col.count(False)
                new_col.append([False]*false_cnt + [c for c in col if c != False])
            
            board = [[0]*n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    board[x][y] = new_col[y][x]
            
            block_pang = []

    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m, n, board))