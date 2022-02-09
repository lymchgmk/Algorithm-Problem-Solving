import sys
sys.stdin = open("9095_1,2,3 더하기.txt", "rt")


def solution(n):
    DP = [0, 1, 2, 4]
    if n <= 3:
        return DP[n]

    DP += [0] * (n-3)
    for i in range(4, n+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    return DP[n]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solution(n))
