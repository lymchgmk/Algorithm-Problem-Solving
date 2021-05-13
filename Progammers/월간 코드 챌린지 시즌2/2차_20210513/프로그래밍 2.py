def solution(numbers):
    answer = []
    for num in numbers:
        _add = 1
        chk = num + _add
        while not 1 <= str(bin(num^chk)).count('1') <= 2:
            _add *= 2
            chk = num + _add
        answer.append(chk)
    return answer


numbers = [2, 7]
print(solution(numbers))
