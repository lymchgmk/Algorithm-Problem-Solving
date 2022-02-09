import sys
sys.stdin = open("11057_오르막 수.txt", "rt")


def solution(N):
    DP = [[1] + [0]*9 for _ in range(N+2)]
    for r in range(1, N+2):
        for c in range(1, 10):
            DP[r][c] += DP[r-1][c] + DP[r][c-1]
    return DP[-1][-1] % 10007


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N = int(input())
    print(solution(N))
