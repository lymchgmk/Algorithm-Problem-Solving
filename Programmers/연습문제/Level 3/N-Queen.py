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


def n_queens (i, col):
    n = len(col) -1
    if promising(col, i):
        if i == n:
            print(col[1: n + 1])
    else:
        for j in range(1, n+1):
            col[i + 1] = j
            n_queens(col, i + 1)

def promising (i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
            k += 1
    return flag