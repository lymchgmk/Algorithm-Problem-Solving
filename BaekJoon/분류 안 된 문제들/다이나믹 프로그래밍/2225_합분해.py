import sys
sys.stdin = open("2225_합분해.txt", "rt")


def solution(N, K):
    dp = [[1]*(N+1)] + [[1] + [0]*N for _ in range(K-1)]
    for r in range(1, K):
        for c in range(1, N+1):
            dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1000000000
    return dp[K-1][N]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N, K = map(int, input().split())
    print(solution(N, K))
