def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0
    while left <= right:
        prev_rock = 0
        min_dist = float('inf')
        removed_rocks = 0
        
        mid = (left+right)//2
        for now_rock in rocks:
            if now_rock - prev_rock < mid:
                removed_rocks += 1
            else:
                min_dist = min(min_dist, now_rock - prev_rock)
                prev_rock = now_rock
        
        if removed_rocks > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = min_dist

    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))