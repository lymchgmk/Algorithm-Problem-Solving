def solution(board, skill):
    R, C = len(board), len(board[0])
    pSum = [[0] * (C+1) for _ in range(R+1)]
    for type, r1, c1, r2, c2, degree in skill:
        degree = degree * -1 if type == 1 else degree
        pSum[r1][c1] += degree
        pSum[r2+1][c1] -= degree
        pSum[r1][c2+1] -= degree
        pSum[r2+1][c2+1] += degree

    for _c in range(C+1):
        for _r in range(1, R+1):
            pSum[_r][_c] += pSum[_r-1][_c]

    for _r in range(R+1):
        for _c in range(1, C+1):
            pSum[_r][_c] += pSum[_r][_c-1]

    answer = 0
    for r in range(R):
        for c in range(C):
            board[r][c] += pSum[r][c]
            if board[r][c] > 0:
                answer += 1
    return answer


if __name__ == "__main__":
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill)) # 10
