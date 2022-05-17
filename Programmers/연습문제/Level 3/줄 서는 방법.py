def solution(n, k):
    from math import factorial
    answer = []
    sample = list(range(1, n+1))
    while n:
        fact = factorial(n-1)
        answer.append(sample.pop((k-1)//fact))
        n -= 1
        k %= fact
    return answer


n = 3
k = 5
print(solution(n, k))