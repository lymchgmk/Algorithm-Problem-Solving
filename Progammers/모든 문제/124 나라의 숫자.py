def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer


print(solution(0))

for i in range(1, 11):
    print(solution(i))

