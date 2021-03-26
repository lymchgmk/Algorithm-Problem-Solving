def solution(dirs):
    visited = []
    now_x, now_y = 0, 0
    dirs_dict = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for key in dirs:
        dir_x, dir_y = dirs_dict[key]
        next_x, next_y = now_x + dir_x, now_y + dir_y
        next_move = set(((now_x, now_y), (next_x, next_y)))
        if -5<=next_x<=5 and -5<=next_y<=5:
            if next_move not in visited:
                visited.append(next_move)
            now_x, now_y = next_x, next_y
    
    return len(visited)


dirs = 	"LULLLLLLU"
print(solution(dirs))
