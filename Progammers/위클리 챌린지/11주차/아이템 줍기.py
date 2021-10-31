def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = [[0] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, [x1, y1, x2, y2])
        for x in range(x1, x2+1):
            if grid[x][y1] == 0:
                grid[x][y1] = 1
            if grid[x][y2] == 0:
                grid[x][y2] = 1
        for y in range(y1, y2+1):
            if grid[x1][y] == 0:
                grid[x1][y] = 1
            if grid[x2][y] == 0:
                grid[x2][y] = 1
        for inner_x in range(x1+1, x2):
            for inner_y in range(y1+1, y2):
                grid[inner_x][inner_y] = 2


    characterX, characterY, itemX, itemY = map(lambda x: x*2, [characterX, characterY, itemX, itemY])
    Q = [(0, characterX, characterY)]
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    answer = float('inf')
    while Q:
        curr_dist, curr_X, curr_Y = Q.pop()
        for dir_x, dir_y in dirs:
            post_X, post_Y = curr_X + dir_x, curr_Y + dir_y
            post_dist = curr_dist + 1
            if 0<=post_X<=50 and 0<=post_Y<=50 and grid[post_X][post_Y] == 1:
                if post_X == itemX and post_Y == itemY:
                    answer = min(answer, post_dist)
                else:
                    grid[post_X][post_Y] = 0
                    Q.append((post_dist, post_X, post_Y))
    return answer // 2


'''
import itertools


def is_movable(cur_x, cur_y, next_x, next_y, rectangles):
    x, y = (cur_x + next_x) / 2, (cur_y + next_y) / 2
    is_on_any_border = any(
        (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
        for x1, y1, x2, y2 in rectangles)
    is_inside_any_rect = any(
        x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangles)
    return is_on_any_border and not is_inside_any_rect


def solution(rectangle, characterX, characterY, itemX, itemY):
    cur_pos = (characterX, characterY)
    prev_pos = None
    for dist in itertools.count():
        if cur_pos == (characterX, characterY) and prev_pos:
            perimeter = dist
            break
        elif cur_pos == (itemX, itemY):
            dist_to_item = dist
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            if next_pos != prev_pos and is_movable(*cur_pos, *next_pos,
                                                   rectangle):
                prev_pos, cur_pos = cur_pos, next_pos
                break
    return min(dist_to_item, perimeter - dist_to_item)
'''

if __name__ == "__main__":
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8
    # 17
    print(solution(rectangle, characterX, characterY, itemX, itemY))