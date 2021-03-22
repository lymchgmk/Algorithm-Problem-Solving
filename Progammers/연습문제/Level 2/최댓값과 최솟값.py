def solution(s):
    s = list(map(int, s.split()))
    _max, _min = max(s), min(s)
    return str(_min) + ' ' + str(_max)


s = '1 2 3 4'
print(solution(s))