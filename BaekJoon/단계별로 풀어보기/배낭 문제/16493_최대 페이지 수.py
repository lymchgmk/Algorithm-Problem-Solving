import sys
sys.stdin = open('16493_최대 페이지 수.txt', 'rt')


def solution(N, M, books):
    dp = [[0] * (N+1) for _ in range(M+1)]
    for i in range(1, M+1):
        cost, pages = books[i-1]
        for j in range(1, N+1):
            if j - cost >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + pages)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[M][N]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    books = [map(int, input().split()) for _ in range(M)]
    print(solution(N, M, books))
