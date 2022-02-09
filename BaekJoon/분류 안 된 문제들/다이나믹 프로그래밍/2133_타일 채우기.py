import sys
sys.stdin = open("2133_타일 채우기.txt", "rt")


def solution(N):
    if N % 2 == 1:
        return 0

    DP = [0] * 31
    DP[0] = 1
    DP[2] = 3
    for i in range(4, N+1):
        if i % 2 == 0:
            DP[i] += 3 * DP[i-2]
            for j in range(0, i-2, 2):
                DP[i] += 2 * DP[j]
    return DP[N]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N = int(input())
    print(solution(N))