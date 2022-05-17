def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if int(num**0.5) == num**0.5:
            answer -= num
        else:
            answer += num
    return answer


left = 13
right = 17
print(solution(left, right))
