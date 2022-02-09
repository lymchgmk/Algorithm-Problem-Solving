import sys
sys.stdin = open("2193_이친수.txt", "rt")


def solution(n):
    DP0 = [0, 0, 1, 1, 2] + [0] * 86
    DP1 = [0, 1, 0, 1, 1] + [0] * 86

    if n <= 4:
        return DP0[n] + DP1[n]

    for i in range(5, n+1):
        DP0[i] = DP0[i-1] + DP1[i-1]
        DP1[i] = DP0[i-1]

    return DP0[n] + DP1[n]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    n = int(input())
    print(solution(n))
