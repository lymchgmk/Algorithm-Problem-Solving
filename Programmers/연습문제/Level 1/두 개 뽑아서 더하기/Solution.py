def solution(numbers):
    answer = []
    L = len(numbers)
    for i in range(L):
        for j in range(i+1, L):
            _sum = numbers[i] + numbers[j]
            if _sum not in answer:
                answer.append(_sum)
    answer.sort()
    return answer