def solution(n):
    n -= 1
    answer = [[0]*(n+2) for _ in range(n+2)]
    dirs = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
    loc_x, loc_y = 0, 0
    num = 1
    dir_idx = 0
    for i in range(n+1, 0, -1):
        dir_x, dir_y = dirs[dir_idx]
        for j in range(i, 0, -1):
            loc_x += dir_x
            loc_y += dir_y
            answer[loc_x][loc_y] += num
            num += 1
        dir_idx = (dir_idx+1)%3
        
    result = []
    for row in answer:
        for num in row:
            if num:
                result.append(num)
    return result


n = 4
print(solution(n))