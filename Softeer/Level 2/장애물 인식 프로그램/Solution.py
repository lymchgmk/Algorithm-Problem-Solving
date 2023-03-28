import sys


def dfs(r, c):
    global visited, count_blocks, total_blocks

    stack = [(r, c)]
    visited[r][c] = True
    count = 1

    while stack:
        curr_r, curr_c = stack.pop()
        for dir_r, dir_c in dirs:
            post_r, post_c = curr_r + dir_r, curr_c + dir_c
            if (0 <= post_r < N and 0 <= post_c < N) and arr[post_r][post_c] and not visited[post_r][post_c]:
                visited[post_r][post_c] = True
                stack.append((post_r, post_c))
                count += 1

    count_blocks.append(count)
    total_blocks += 1


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited = [[False] * N for _ in range(N)]

    count_blocks = []
    total_blocks = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] and not visited[r][c]:
                dfs(r, c)

    print(total_blocks)
    for count in sorted(count_blocks):
        print(count)