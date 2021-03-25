def solution(n):
    return bin(n)[2:].count('1')


N = 5000
print(solution(N))