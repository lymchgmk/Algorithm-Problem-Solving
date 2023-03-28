import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N = int(input())
    dp = [0] * 16
    dp[0], dp[1], dp[2] = 2, 3, 5
    for i in range(N+1):
        if not dp[i]:
            dp[i] = dp[i-1] * 2 - 1

    print(dp[N] * dp[N])
