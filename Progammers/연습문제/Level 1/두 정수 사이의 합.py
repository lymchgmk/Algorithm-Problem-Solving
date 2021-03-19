def solution(a, b):
    answer = 0
    a, b = min(a, b), max(a, b)
    for n in range(a, b+1):
        answer += n
    return answer