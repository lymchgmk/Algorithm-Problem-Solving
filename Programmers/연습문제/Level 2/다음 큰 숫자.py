def solution(n):
    answer = n+1
    while str(bin(answer)).count('1') != str(bin(n)).count('1'):
        answer += 1
    return answer


n = 78
print(solution(n))