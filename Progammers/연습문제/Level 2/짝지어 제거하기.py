def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    
    return 1 if not stack else 0


def solution_re(s):
    import re
    while s:
        re_sub_s = re.sub(r'(\w)(\1)', '', s)
        if s == re_sub_s:
            break
        s = re_sub_s
    return 1 if not s else 0
    
    
    
    
    


s = 'cdcd'
print(solution(s))
print(solution_re(s))