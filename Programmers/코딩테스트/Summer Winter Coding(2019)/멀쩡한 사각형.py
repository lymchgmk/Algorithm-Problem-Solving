import math


def solution(w,h):
    a = h/w
    answer = w*h
    for i in range(1, w+1):
        answer -= math.ceil(a*i) - math.floor(a*(i-1))
    return answer


w = 8
h = 12
print(solution(w, h))