def solution(n, build_frame):
    def can_build(x, y, a):
        if a == 0:
            if x == 0 or board[x-1][y] == 1:
                return True
        else:
            if board[x][y] == 1 or board[x][y]
    
    answer = [[]]
    board = [[0]*(n+1) for _ in range(n+1)]
    
    for b in board:
        print(b)
    print()
    
    for x, y, a, b in build_frame:
        # a: 0 기둥, 1 보 / b: 0 삭제, 1 설치
        print(x, y, a, b)
        if a == 0:
            if b == 0:
                board[x][y] = board[x - 1][y] = 0
            else:
                board[x][y] = board[x - 1][y] = 1
                
        else:
            if b == 0:
                board[x][y] = board[x][y-1] = 0
            else:
                board[x][y] = board[x][y-1] = 1
            
        for b in board:
            print(b)
        print()
        
    for i in range(n+1):
        for j in range(n+1):
            pass
    
    return answer


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))