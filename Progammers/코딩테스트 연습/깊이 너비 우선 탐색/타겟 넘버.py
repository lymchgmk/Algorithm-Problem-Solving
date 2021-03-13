def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(idx, value):
        global answer
        L = len(numbers)
        if idx == L:
            if target == value:
                answer += 1
            return
        dfs(idx+1, value + numbers[idx])
        dfs(idx+1, value - numbers[idx])
    
    dfs(0, 0)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
