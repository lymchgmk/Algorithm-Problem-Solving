def solution(n):
    return len([i for i in range(1, n+1, 2) if not n%i])


n = 15
print(solution(n))