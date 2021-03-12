def solution(numbers):
    answer = []
    N = len(numbers)
    for i in range(N):
        for j in range(N):
            if i != j:
                temp = numbers[i] + numbers[j]
                if temp not in answer:
                    answer.append(temp)
    answer.sort()
    return answer