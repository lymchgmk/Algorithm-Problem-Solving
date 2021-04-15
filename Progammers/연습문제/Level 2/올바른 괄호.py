def solution(s):
    answer = True
    Queue = []
    for i in s:
        if i == '(':
            Queue.append('(')
        else:
            try:
                Queue.pop()
            except ValueError:
                return False
            
    if len(Queue) == 0:
        return True
    else:
        return False


s = '()()'
print(solution(s))
