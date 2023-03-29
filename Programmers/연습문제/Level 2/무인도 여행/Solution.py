dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def solution(maps):
    def dfs(r, c, count):
        nonlocal visited

        stack = [(r, c, count)]
        while stack:
            curr_r, curr_c, curr_count = stack.pop()
            visited[curr_r][curr_c] = True

            for dir_r, dir_c in dirs:
                post_r, post_c = curr_r + dir_r, curr_c + dir_c

                if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and not visited[post_r][post_c]:
                    post_count = curr_count + maps[post_r][post_c]




    MAX_R, MAX_C = len(maps), len(maps[0])
    visited = [[False] * MAX_C for _ in range(MAX_R)]
    islands = []

    for r in range(MAX_R):
        for c in range(MAX_C):
            if not visited[r][c]:
                dfs(r, c, int(maps[r][c]))

    return islands if islands else [-1]


if __name__ == "__main__":
    maps = ["X591X","X1X5X","X231X", "1XXX1"]
    result = [1, 1, 27]
    answer = solution(maps)
    print(f"[{answer == result}] {answer}")
