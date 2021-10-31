import heapq


def solution(rectangle, characterX, characterY, itemX, itemY):
    grid = [[0] * 51 for _ in range(51)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2+1):
            grid[x][y1] = 1
            grid[x][y2] = 1
        for y in range(y1, y2+1):
            grid[x1][y] = 1
            grid[x2][y] = 1
        for inner_x in range(x1+1, x2):
            for inner_y in range(y1+1, y2):
                grid[inner_x][inner_y] = 0

    HQ = []
    heapq.heappush(HQ, (0, characterX, characterY))
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    answer = float('inf')
    while HQ:
        curr_dist, curr_X, curr_Y = heapq.heappop(HQ)
        for dir_x, dir_y in dirs:
            post_X, post_Y = curr_X + dir_x, curr_Y + dir_y
            post_dist = curr_dist + 1
            if 0<=post_X<=50 and 0<=post_Y<=50 and grid[post_X][post_Y] == 1:
                if post_X == itemX and post_Y == itemY:
                    answer = min(answer, post_dist)
                else:
                    grid[post_X][post_Y] = 0
                    heapq.heappush(HQ, (post_dist, post_X, post_Y))
    return answer


if __name__ == "__main__":
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8
    # 17
    print(solution(rectangle, characterX, characterY, itemX, itemY))