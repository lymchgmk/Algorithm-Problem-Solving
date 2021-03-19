def solution(arr):
    answer = []
    chk = -1
    for num in arr:
        if num != chk:
            answer.append(num)
            chk = num
    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))