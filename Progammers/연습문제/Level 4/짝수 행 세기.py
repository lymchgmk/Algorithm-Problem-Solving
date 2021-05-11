def solution(a):
    r, c = len(a), len(a[0])
    dp = [[0]*c for _ in range(r)]
    Arr_OneCnt = [sum([row[i] for row in a]) for i in range(c)]
    
    
    


a = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
print(solution(a))
