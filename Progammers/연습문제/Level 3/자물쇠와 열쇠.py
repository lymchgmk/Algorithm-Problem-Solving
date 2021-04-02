def solution(key, lock):
    def make_rotated_keys(key):
        rotated_keys = [key]
        tmp_key = key
        for angle in range(1, 4):
            res = [[0] * L for _ in range(L)]
            for i in range(L):
                col = [row[i] for row in tmp_key]
                for j in range(L):
                    res[i][j] = col[::-1][j]
            rotated_keys.append(res)
            tmp_key = res
        return rotated_keys
    
    def match(lock, rotated_key, point):
        board = [[0]*(3*L-2) for _ in range(3*L-2)]
        for i in range(L-1, 2*L-1):
            for j in range(L-1, 2*L-1):
                board[i][j] += lock[i-L+1][j-L+1]
        
        for i in range(L):
            for j in range(L):
                i_rk, j_rk = i+point[0], j+point[1]
                board[i_rk][j_rk] += rotated_key[i][j]
        
        for i in range(L-1, 2*L-1):
            for j in range(L-1, 2*L-1):
                if board[i][j] != 1:
                    return False
        else:
            return True
        
    
    L = len(lock)
    rotated_keys = make_rotated_keys(key)
    for rk in rotated_keys:
        for i in range(2*L-1):
            for j in range(2*L-1):
                if match(lock, rk, [i, j]):
                    return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
