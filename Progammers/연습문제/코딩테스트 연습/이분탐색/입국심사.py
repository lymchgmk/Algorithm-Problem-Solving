def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * (n//len(times) + 1)
    while left <= right:
        mid = (left+right)//2
        
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
                
        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


n = 6
times = [7, 10]
print(solution(n, times))
