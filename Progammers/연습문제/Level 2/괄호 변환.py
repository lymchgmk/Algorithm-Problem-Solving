def solution(p):
    def isProper(u):
        stack = []
        for char in u:
            if char == '(':
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    stack.pop()
        return True
    
    # 1
    if not p:
        return ''
    
    # 2
    u, v = p[:1], p[1:]
    idx = 1
    while u.count('(') != u.count(')'):
        idx += 1
        u = p[:idx]
        v = p[idx:]
    
    # 3.
    if isProper(u):
        return u + solution(v)
    
    # 4.
    else:
        answer = '(' + solution(v) + ')'
        for char in u[1:-1]:
            if char == '(':
                answer += ')'
            else:
                answer += '('
        return answer
        

p = "()))((()"
print(solution(p))