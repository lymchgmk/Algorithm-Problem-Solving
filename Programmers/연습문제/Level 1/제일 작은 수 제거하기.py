def solution(arr):
    answer= []
    _min = min(arr)
    for n in arr:
        if n != _min:
            answer.append(n)
    
    return answer if answer else [-1]