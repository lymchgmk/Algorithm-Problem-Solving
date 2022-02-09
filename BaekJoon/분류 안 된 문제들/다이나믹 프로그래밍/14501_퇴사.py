import sys
sys.stdin = open("14501_퇴사.txt", "rt")


def solution(N, T, P):
    dp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        if T[i] + i <= N:
            dp[i] = max(P[i] + dp[T[i] + i], dp[i+1])
        else:
            dp[i] = dp[i+1]
    return dp[0]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N = int(input())
    TP = [map(int, input().split()) for _ in range(N)]
    T, P = list(zip(*TP))
    print(solution(N, T, P))
