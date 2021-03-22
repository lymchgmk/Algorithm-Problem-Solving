def solution(s):
    q = []
    for char in s:
        if char == '(':
            q.append(char)
        else:
            try:
                q.pop()
            except IndexError:
                return False
    
    if not len(q):
        return True
    else:
        return False


s = '()()'
print(solution(s))