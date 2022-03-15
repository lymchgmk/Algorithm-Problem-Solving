import sys
sys.stdin = open("1890_점프.txt", "rt")


def solution(N, arr):
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1
    for r in range(N):
        for c in range(N):
            jump = arr[r][c]
            if (r, c) == (N-1, N-1):
                print(dp[N-1][N-1])
                return
            if r + jump < N:
                dp[r+jump][c] += dp[r][c]
            if c + jump < N:
                dp[r][c+jump] += dp[r][c]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solution(N, arr)
