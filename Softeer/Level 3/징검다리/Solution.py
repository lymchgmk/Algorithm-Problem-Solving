import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N = int(input())
    A = list(map(int, input().split()))

    dp = [1] * N
    for i in range(1, N):
        for j in range(0, i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
