import sys
sys.stdin = open('12865_평범한 배낭.txt', 'rt')


def solution(N, K, items):
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        W, V = items[i-1]
        for j in range(1, K+1):
            if j >= W:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][K]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())
    items = [map(int, input().split()) for _ in range(N)]
    print(solution(N, K, items))
