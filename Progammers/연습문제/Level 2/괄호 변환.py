def solution(p):
    def isBalanced():
        pass
    
    def isProper():
        pass
    
    # 1
    if not p:
        return p
    
    # 2
    u, v = p[:1], p[1:]
    idx = 1
    while u.count('(') != u.count(')'):
        idx += 1
        u = p[:idx]
        v = p[idx:]
    
    # 3.
    if isProper(u):
        answer += u + solution(v)
    
    return 0


p = "()))((()"
print(solution(p))