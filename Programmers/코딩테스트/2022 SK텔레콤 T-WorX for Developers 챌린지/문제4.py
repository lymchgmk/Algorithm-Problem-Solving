from collections import deque


def solution(grid, k):
    answer = len(grid) * len(grid[0])
    routes = getRoutes(grid, k)
    for route in routes:
        answer = min(answer, getMinCamp(route, k))
    return answer


def getRoutes(grid, k):
    grid = [list(row) for row in grid]
    max_r, max_c = len(grid), len(grid[0])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    answer = max_r * max_c
    dq = deque([(0, 0, grid[0][0])])
    grid[0][0] = '#'
    routes = []
    while dq:
        curr_r, curr_c, curr_route = dq.popleft()
        for dir_r, dir_c in dirs:
            post_r, post_c = curr_r + dir_r, curr_c + dir_c
            if (0<=post_r<max_r and 0<=post_c<max_c) and grid[post_r][post_c] != '#':
                post_route = curr_route + grid[post_r][post_c]
                if post_r == max_r - 1 and post_c == max_c - 1:
                    routes.append(post_route)
                    continue
                grid[post_r][post_c] = '#'
                dq.append((post_r, post_c, post_route))
    return routes


def getMinCamp(route, k):
    minCamp = 0
    idx, step = 0, 0
    while True:
        idx += k
        if idx >= len(route) - 1:
            return minCamp
        
        while idx < len(route) - 1 and route[idx] != '.':
            idx -= 1
        minCamp += 1
            

if __name__ == "__main__":
    grid = [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"]
    k = 6
    # grid = ["..FF", "###F", "###."]
    # k = 4
    print(solution(grid, k)) # 3