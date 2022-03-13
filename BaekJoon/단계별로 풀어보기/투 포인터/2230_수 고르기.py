import sys
sys.stdin = open("2230_수 고르기.txt", 'rt')


def solution(N, M, A):
    def gap(l, r):
        return A[r] - A[l]

    A.sort()
    answer = A[-1] - A[0]
    left = right = 0
    while left < len(A):
        if gap(left, right) >= M:
            answer = min(answer, gap(left, right))

        if gap(left, right) < M and right < len(A) - 1:
            right += 1
        else:
            left += 1
    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    solution(N, M, A)
