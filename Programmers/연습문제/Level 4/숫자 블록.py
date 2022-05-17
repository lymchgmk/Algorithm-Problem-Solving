def solution(begin, end):
    def quotient(n):
        for div in range(2, int(n**0.5)+1):
            q, r = divmod(n, div)
            if q > 10000000:
                continue
            if r == 0:
                return q
        return 0 if n == 1 else 1

    return [quotient(n) for n in range(begin, end + 1)]


begin = 1
end = 10
print(solution(begin, end))