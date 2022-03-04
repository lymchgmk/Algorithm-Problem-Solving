import sys
sys.stdin = open('11659_구간 합 구하기 4.txt', 'rt')


def make_ps(arr):
    res = [0] * (N + 1)
    for i in range(N):
        res[i+1] = res[i] + arr[i]
    return res


def solution(i, j, arr):
    global partial_sum
    return partial_sum[j] - partial_sum[i-1]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    partial_sum = make_ps(arr)
    for _ in range(M):
        i, j = map(int, input().split())
        print(solution(i, j, arr))
