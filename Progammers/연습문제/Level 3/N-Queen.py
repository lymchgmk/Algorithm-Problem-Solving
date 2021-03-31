def solution(n):
    def queens(n, i=0, a=[], b=[], c=[]):
        if i < n:
            for j in range(n):
                if j not in a and i + j not in b and i - j not in c:
                    yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
        else:
            yield a
    
    return sum([1 for _ in queens(n)])

print(solution(5))