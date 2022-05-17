def solution(maps):
    from collections import deque
   
    n, m = len(maps), len(maps[0])
    deq = deque([[0, 0]])
    maps[0][0] = 1
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while deq:
        if maps[n-1][m-1] != 1:
            break
            
        now_x, now_y = deq.popleft()
        for dir_x, dir_y in dirs:
            next_x, next_y = now_x + dir_x, now_y + dir_y
            if 0<=next_x<n and 0<=next_y<m and maps[next_x][next_y] == 1:
                maps[next_x][next_y] = maps[now_x][now_y] + 1
                deq.append([next_x, next_y])
        
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))