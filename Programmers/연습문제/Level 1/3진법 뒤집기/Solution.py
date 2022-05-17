def solution(n):
    res = ""
    while n:
        q, r = divmod(n, 3)
        n = q
        res += str(r)
    return int(res, 3)
