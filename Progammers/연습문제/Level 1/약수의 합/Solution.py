def solution(n):
    answer = 0
    for div in range(1, n+1):
        if not n % div:
            answer += div
    return answer