import sys
sys.stdin = open("11052_카드 구매하기.txt", "rt")


def solution(N, P):
    DP = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, i+1):
            DP[i] = max(DP[i], DP[i-j] + P[j])
    return DP[N]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N = int(input())
    P = [0] + list(map(int, input().split()))
    print(solution(N, P))