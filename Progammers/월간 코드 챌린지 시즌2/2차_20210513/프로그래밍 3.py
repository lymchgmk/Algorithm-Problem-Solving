import re


def solution(s):
    for sample in s:
        flag = True
        _find = [f.span() for f in re.finditer('110', sample)]
        print(_find)


s = ["1110","100111100","0111111010110"]
print(solution(s))
