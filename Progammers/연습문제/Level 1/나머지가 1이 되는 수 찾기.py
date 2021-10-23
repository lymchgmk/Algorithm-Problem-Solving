def solution(n):
    for d in range(2, n):
        if (n-1) % d == 0:
            return d