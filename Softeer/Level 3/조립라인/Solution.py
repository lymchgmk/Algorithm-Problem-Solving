import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N-1)]
    last_work = list(map(int, input().split()))

    INF = float('inf')
    dp_A = [0] * N
    dp_B = [0] * N
    for i in range(N-1):
        dp_A[i] += works[i][0]
        dp_B[i] += works[i][1]
        dp_A[i+1] = min(dp_A[i], dp_B[i] + works[i][3])
        dp_B[i+1] = min(dp_B[i], dp_A[i] + works[i][2])

    print(min(dp_A[-1] + last_work[0], dp_B[-1] + last_work[1]))
