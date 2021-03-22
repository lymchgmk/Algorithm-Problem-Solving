def solution(arr):
    import math
    answer = arr.pop()
    while arr:
        temp = arr.pop()
        answer = answer * temp // math.gcd(answer, temp)
    
    return answer


arr = [1,2,3]
print(solution(arr))