def solution(s):
    import re
    answer = ''
    pattern = r'([\w\d])([\w\d]+)?(\s+)?'
    for pre, suf, blank in re.findall(pattern, s):
        answer += pre.upper() + suf.lower() + blank
    return answer
    
    
    
    


s = "3people unFollowed me"
print(solution(s))