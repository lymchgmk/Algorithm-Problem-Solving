def solution(key, lock):
    def rotate(key, angle):
        angle //= 90
        res = [[0]*len(key) for _ in range(len(key))]
        while angle:
            for i in range(len(key)):
                col = [row[i] for row in key]
                for j in range(len(key)):
                    res[i][j] = col[::-1][j]
            angle -= 1
        return res
    
    def match(lock, k):
        pass
    
    L = len(lock)
    keys = (key, rotate(key, 90), rotate(key, 180), rotate(key, 270))
    for k in keys:
        if match(lock, k):
            return True
    return False
