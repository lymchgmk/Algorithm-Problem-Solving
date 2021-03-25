def solution(p):
    # 1
    if not p:
        return p
    
    # 2
    u, v = '', ''
    idx = 0
    while True:
        idx += 1
        u = p[:idx]
        if u.count('(') == u.count(')'):
            break
    
    # 3.
    if 
    
    return 0


p = "()))((()"
print(solution(p))