def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        move -= 1
        for depth in range(len(board)):
            doll = board[depth][move]
            if doll != 0:
                bucket.append(doll)
                board[depth][move] = 0
                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    answer += 2
                break
    return answer


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves)) # 4