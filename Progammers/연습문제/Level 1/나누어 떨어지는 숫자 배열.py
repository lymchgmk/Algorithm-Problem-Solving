def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num % divisor:
            answer.append(num)
    
    answer.sort()
    if not answer:
        return [-1]
    
    return answer