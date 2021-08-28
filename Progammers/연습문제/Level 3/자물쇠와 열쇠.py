def solution(key, lock):
    def _make_rotated_keys(key):
        res = [key]
        for _ in range(3):
            key = list(zip(*key[::-1]))
            res.append([list(row) for row in key])
        return res
    
    def match(lock, rotated_key, point):
        board = [[0] * (L + 2 * K - 2) for _ in range(L + 2 * K - 2)]
        for i in range(K - 1, K + L - 1):
            for j in range(K - 1, K + L - 1):
                board[i][j] += lock[i - K + 1][j - K + 1]
        
        for i in range(K):
            for j in range(K):
                i_rk, j_rk = i + point[0], j + point[1]
                board[i_rk][j_rk] += rotated_key[i][j]
        
        for i in range(K - 1, K + L - 1):
            for j in range(K - 1, K + L - 1):
                if board[i][j] != 1:
                    return False
        else:
            return True
    
    L, K = len(lock), len(key)
    rotated_keys = _make_rotated_keys(key)
    for rk in rotated_keys:
        for i in range(L + K - 1):
            for j in range(L + K - 1):
                if match(lock, rk, [i, j]):
                    return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
