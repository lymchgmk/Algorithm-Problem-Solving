RED_START, BLUE_START, RED_END, BLUE_END = 1, 2, 3, 4
EMPTY, WALL = 0, 5
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
INF = float('inf')


def solution(maze: [[int]]) -> int:
    positions = get_positions(maze)
    min_turn = calc_min_turn(maze, positions)
    return min_turn


def get_positions(maze: [[int]]) -> {int: int}:
    positions = {}
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            grid = maze[r][c]
            if grid != EMPTY:
                positions[grid] = (r, c)

    return positions


def calc_min_turn(maze: [[int]], positions: {int: (int, int)}) -> int:

    def _dfs(turn: int, maze: [[int]], curr_red_pos: (int, int), curr_blue_pos: (int, int), red_visited: [[bool]], blue_visited: [[bool]]):
        nonlocal red_end, blue_end, min_turn

        red_visited[curr_red_pos[0]][curr_red_pos[1]] = blue_visited[curr_blue_pos[0]][curr_blue_pos[1]] = True

        if curr_red_pos == red_end and curr_blue_pos == blue_end:
            min_turn = min(min_turn, turn)
            return
        elif curr_red_pos == red_end and curr_blue_pos != blue_end:
            for blue_dir_r, blue_dir_c in DIRS:
                post_blue_pos = (curr_blue_pos[0] + blue_dir_r, curr_blue_pos[1] + blue_dir_c)

                if can_move(maze, curr_red_pos, post_blue_pos, red_visited, blue_visited):
                    blue_visited[post_blue_pos[0]][post_blue_pos[1]] = True
                    _dfs(turn + 1, maze, curr_red_pos, post_blue_pos, red_visited, blue_visited)
                    blue_visited[post_blue_pos[0]][post_blue_pos[1]] = False
        elif curr_red_pos != red_end and curr_blue_pos == blue_end:
            for red_dir_r, red_dir_c in DIRS:
                post_red_pos = (curr_red_pos[0] + red_dir_r, curr_red_pos[1] + red_dir_c)

                if can_move(maze, post_red_pos, curr_blue_pos, red_visited, blue_visited):
                    red_visited[post_red_pos[0]][post_red_pos[1]] = True
                    _dfs(turn + 1, maze, post_red_pos, curr_blue_pos, red_visited, blue_visited)
                    red_visited[post_red_pos[0]][post_red_pos[1]] = False
        else: # if curr_red_pos != red_end and curr_blue_pos != blue_end
            for red_dir_r, red_dir_c in DIRS:
                for blue_dir_r, blue_dir_c in DIRS:
                    post_red_pos = (curr_red_pos[0] + red_dir_r, curr_red_pos[1] + red_dir_c)
                    post_blue_pos = (curr_blue_pos[0] + blue_dir_r, curr_blue_pos[1] + blue_dir_c)

                    if curr_red_pos == post_blue_pos and post_red_pos == curr_blue_pos:
                        continue

                    if can_move(maze, post_red_pos, post_blue_pos, red_visited, blue_visited):
                        red_visited[post_red_pos[0]][post_red_pos[1]] = blue_visited[post_blue_pos[0]][
                            post_blue_pos[1]] = True
                        _dfs(turn + 1, maze, post_red_pos, post_blue_pos, red_visited, blue_visited)
                        red_visited[post_red_pos[0]][post_red_pos[1]] = blue_visited[post_blue_pos[0]][
                            post_blue_pos[1]] = False

    def can_move(maze: [[int]], red_pos: (int, int), blue_pos: (int, int), red_visited: [[bool]],
                 blue_visited: [[bool]]) -> bool:
        nonlocal red_end, blue_end

        _max_r, _max_c = len(maze), len(maze[0])
        if not (0 <= red_pos[0] < _max_r and 0 <= red_pos[1] < _max_c and 0 <= blue_pos[0] < _max_r and 0 <=
                blue_pos[1] < _max_c):
            return False

        if maze[red_pos[0]][red_pos[1]] == WALL or maze[blue_pos[0]][blue_pos[1]] == WALL:
            return False

        if red_pos == blue_pos:
            return False

        if (red_pos != red_end and red_visited[red_pos[0]][red_pos[1]]) or (
                blue_pos != blue_end and blue_visited[blue_pos[0]][blue_pos[1]]):
            return False

        return True

    red_start, blue_start = positions[RED_START], positions[BLUE_START]
    red_visited, blue_visited = [[False] * len(maze[0]) for _ in range(len(maze))], [[False] * len(maze[0]) for _ in range(len(maze))]
    red_end, blue_end = positions[RED_END], positions[BLUE_END]
    min_turn = INF
    _dfs(0, maze, red_start, blue_start, red_visited, blue_visited)

    return min_turn if min_turn != INF else 0


if __name__ == "__main__":
    # maze = [[1, 4], [0, 0], [2, 3]]
    # result = 3

    # maze = [[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]
    # result = 7

    # maze = [[1, 5], [2, 5], [4, 5], [3, 5]]
    # result = 0

    maze = [[4, 1, 2, 3]]
    result = 0

    print(solution(maze))
