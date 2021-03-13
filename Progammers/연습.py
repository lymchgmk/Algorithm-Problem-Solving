def solution(numbers, target):
    global answer
    answer = 0
    
    def DFS(idx, val):
        global answer
        if idx == len(numbers):
            if target == val:
                answer += 1
            return
        
        DFS(idx+1, val+numbers[idx])
        DFS(idx+1, val-numbers[idx])
    
    DFS(0, 0)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
