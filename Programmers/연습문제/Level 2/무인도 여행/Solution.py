DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solution(maps):
    MAX_R, MAX_C = len(maps), len(maps[0])

    def dfs(start_r, start_c, start_count):
        nonlocal visited

        stack = [(start_r, start_c)]
        visited[start_r][start_c] = True
        counts = start_count
        while stack:
            curr_r, curr_c = stack.pop()
            for dir_r, dir_c in DIRS:
                post_r, post_c = curr_r + dir_r, curr_c + dir_c
                if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and maps[post_r][post_c] != 'X' and not visited[post_r][post_c]:
                    visited[post_r][post_c] = True
                    counts += int(maps[post_r][post_c])
                    stack.append((post_r, post_c))

        return counts

    islands = []
    visited = [[False] * MAX_C for _ in range(MAX_R)]
    for r in range(MAX_R):
        for c in range(MAX_C):
            if maps[r][c] != 'X' and not visited[r][c]:
                islands.append(dfs(r, c, int(maps[r][c])))

    return sorted(islands) if islands else [-1]


if __name__ == "__main__":
    maps = ["X591X","X1X5X","X231X", "1XXX1"]
    result = [1, 1, 27]
    answer = solution(maps)
    print(f"[{answer == result}] {answer}")
