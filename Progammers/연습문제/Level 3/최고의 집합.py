def solution(n, s):
    if n > s:
        return [-1]
    else:
        q, r = divmod(s, n)
        return [q]*(n-r) + [q+1]*r


n = 2
s = 9
print(solution(n, s))