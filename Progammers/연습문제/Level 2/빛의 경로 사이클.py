dx = [1,0,-1,0]
dy = [0,-1,0,1]

def solution(grid):
    def beam(sr, sc, sd):
        global visited
        visited[sr][sc][sd] = True
        nr, nc, nd = sr, sc, sd
        cnt = 0
        while True:
            nr = (nr + dirs[nd][0]) % lr
            nc = (nc + dirs[nd][1]) % lc
            cnt += 1

            if grid[nr][nc] == 'R':
                nd = (nd + 1) % ldir
            elif grid[nr][nc] == 'L':
                nd = (nd - 1) % ldir
            else:
                pass

            if visited[nr][nc][nd]:
                if (nr, nc, nd) == (sr, sc, sd):
                    return cnt
                else:
                    return 0

            visited[nr][nc][nd] = True

    global visited
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    lr, lc, ldir = len(grid), len(grid[0]), len(dirs)
    answer = []
    visited = [[[False]*ldir for _ in range(lc)] for _ in range(lr)]
    for sr in range(lr):
        for sc in range(lc):
            for sd in range(ldir):
                if not visited[sr][sc][sd]:
                    cycle_len = beam(sr, sc, sd)
                    if cycle_len != 0:
                        answer.append(cycle_len)
    return sorted(answer)


if __name__ == "__main__":
    grid = ["SL","LR"]
    print(solution(grid)) # 16