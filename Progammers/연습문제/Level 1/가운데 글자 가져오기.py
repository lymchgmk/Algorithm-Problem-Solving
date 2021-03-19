def solution(s):
    L = len(s)
    return s[(L-1)//2: L//2+1]


s = 'qwer'
print(solution(s))