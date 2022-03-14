import sys
sys.stdin = open("2018_수들의 합 5.txt", 'rt')


def solution(N):
    left = right = 1
    nsum = 1
    cnt = 0
    while left <= right <= N:
        if nsum == N:
            cnt += 1

        if nsum < N:
            right += 1
            nsum += right
        else:
            nsum -= left
            left += 1
    print(cnt)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    solution(N)
