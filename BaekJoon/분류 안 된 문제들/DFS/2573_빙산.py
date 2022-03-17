import sys
sys.stdin = open("2573_빙산.txt", 'rt')


def cnt_bulk(icebergs, dirs):
    _cnt = 0
    visited = [[False]*M for _ in range(N)]
    for start_r in range(1, N-1):
        for start_c in range(1, M-1):
            if not visited[start_r][start_c] and icebergs[start_r][start_c] > 0:
                visited[start_r][start_c] = True
                stack = [(start_r, start_c)]
                while stack:
                    curr_r, curr_c = stack.pop()
                    for d_r, d_c in dirs:
                        post_r, post_c = curr_r + d_r, curr_c + d_c
                        if 1 <= post_r < N-1 and 1 <= post_c < M-1 and not visited[post_r][post_c] and icebergs[post_r][post_c] > 0:
                            visited[post_r][post_c] = True
                            stack.append((post_r, post_c))
                _cnt += 1
    return _cnt


def melt(icebergs, dirs):
    melted_mass = [[0]*M for _ in range(N)]
    for r in range(1, N - 1):
        for c in range(1, M - 1):
            for d_r, d_c in dirs:
                if icebergs[r+d_r][c+d_c] == 0:
                    melted_mass[r][c] -= 1

    all_meltdown = True
    for r in range(1, N-1):
        for c in range(1, M-1):
            icebergs[r][c] = max(icebergs[r][c] + melted_mass[r][c], 0)
            if icebergs[r][c] > 0:
                all_meltdown = False

    return icebergs, all_meltdown


def solution(N, M, icebergs):
    year = 0
    all_meltdown = False
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while not all_meltdown:
        cnt = cnt_bulk(icebergs, dirs)
        if not all_meltdown and cnt >= 2:
            return year

        icebergs, all_meltdown = melt(icebergs, dirs)
        if all_meltdown:
            return 0

        year += 1


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    icebergs = [list(map(int,input().split())) for _ in range(N)]
    print(solution(N, M, icebergs))
