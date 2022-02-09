import sys
sys.stdin = open("11727_2xn 타일링 2.txt", "rt")


def solution(n):
    DP = [0, 1, 3] + [0] * 998
    if n <= 2:
        return DP[n]

    for i in range(3, n+1):
        DP[i] = (DP[i-1] + 2*DP[i-2]) % 10007
    return DP[n]



if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    n = int(input())
    print(solution(n))