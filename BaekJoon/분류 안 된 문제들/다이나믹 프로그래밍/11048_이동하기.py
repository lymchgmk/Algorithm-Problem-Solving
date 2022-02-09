import sys
sys.stdin = open("11048_이동하기.txt", "rt")


def solution(N, M, ARR):
    dirs = ((-1, 0), (0, -1), (-1, -1))
    for r in range(N):
        for c in range(M):
            curr_candies = ARR[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    ARR[r][c] = max(ARR[r][c], curr_candies + ARR[nr][nc])
    return ARR[N-1][M-1]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N, M = map(int, input().split())
    ARR = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, ARR))
