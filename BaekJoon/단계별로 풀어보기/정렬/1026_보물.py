import sys
sys.stdin = open('1026_보물.txt', 'rt')


def solution(N, A, B):
    A.sort()
    B.sort(reverse=True)
    print(sum([A[i] * B[i] for i in range(N)]))


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    solution(N, A, B)
