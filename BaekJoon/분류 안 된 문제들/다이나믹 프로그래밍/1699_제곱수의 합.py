import sys
sys.stdin = open("1699_제곱수의 합.txt", "rt")


def solution(N):
    dp = [n for n in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, i):
            if j**2 > i:
                break
            print(dp, i, j)
            dp[i] = min(dp[i], dp[i - j**2]+1)
    return dp[N]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N = int(input())
    print(solution(N))