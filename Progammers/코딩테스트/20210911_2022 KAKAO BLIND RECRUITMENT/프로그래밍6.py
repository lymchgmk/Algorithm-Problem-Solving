def solution(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += degree

    N, M = len(board), len(board[0])
    answer = 0
    for n in range(N):
        for m in range(M):
            if board[n][m] > 0:
                answer += 1
    return answer


board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))
