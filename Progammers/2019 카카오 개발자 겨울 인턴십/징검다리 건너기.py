# 풀이 1. 이분탐색
def solution_1(stones, k):
    def jump(stones, k, mid):
        jump_count = k
        for stone in stones:
            if stone <= mid:
                jump_count -= 1
                if not jump_count:
                    return False
            else:
                jump_count = k
        return True
    
    answer = 0
    left, right = 0, 200000000
    while left <= right:
        mid = (left+right)//2
        if jump(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer+1


# 풀이 2. 슬라이딩 윈도우
# 이 경우 max 부분에서 시간이 오버됨?
def solution_2(stones, k):
    from collections import deque
    window = deque(stones[:k])
    loc_max = max(window)
    global_min = loc_max
    for i in range(k, len(stones)):
        leftpop = window.popleft()
        window.append(stones[i]) #rightappend
        if leftpop == loc_max:
            loc_max = max(window)
            global_min = min(global_min, loc_max)
    return global_min
    


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution_1(stones, k))