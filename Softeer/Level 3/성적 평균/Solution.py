import sys


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    input = lambda: sys.stdin.readline().strip()

    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    S_sum = [0] + S
    for i in range(1, N+1):
        S_sum[i] += S_sum[i-1]

    for _ in range(K):
        A, B = map(int, input().split())
        answer = round((S_sum[B] - S_sum[A-1]) / (B - A + 1), 2)
        print(f"{answer: .2f}")
