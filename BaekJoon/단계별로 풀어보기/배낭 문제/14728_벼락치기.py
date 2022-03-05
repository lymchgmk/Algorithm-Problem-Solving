import sys
sys.stdin = open('14728_벼락치기.txt', 'rt')


def solution(N, T, KS):
    dp = [[0] * (T+1) for _ in range(N+1)]
    for i in range(1, N+1):
        K, S = KS[i-1]
        for j in range(1, T+1):
            if j >= K:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-K] + S)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][T]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, T = map(int, input().split())
    KS = [map(int, input().split()) for _ in range(N)]
    print(solution(N, T, KS))
