def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        move=i-1
        for j in range(len(board)):
            doll=board[j][move]
            if doll != 0:
                stack.append(doll)
                board[j][move] = 0

                if stack:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2     
                break

    return answer