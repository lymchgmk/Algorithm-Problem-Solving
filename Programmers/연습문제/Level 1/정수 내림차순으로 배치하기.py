def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))


n = 118372
print(solution(n))