from math import factorial as fac


def solution(n):
    return fac(2*n)//(fac(n+1)*fac(n))


n = 3
print(solution(n))
