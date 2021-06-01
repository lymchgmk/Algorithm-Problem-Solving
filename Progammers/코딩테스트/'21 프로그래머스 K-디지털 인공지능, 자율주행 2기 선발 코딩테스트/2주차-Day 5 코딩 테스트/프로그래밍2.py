def solution(arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    answer = 0
    time_check = 0
    for S, E in arr:
        if time_check <= S:
            answer += 1
            time_check = E
    
    return answer


arr = [[1, 2], [2, 4], [2, 2]]
print(solution(arr))