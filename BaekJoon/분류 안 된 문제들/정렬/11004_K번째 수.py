import sys
sys.stdin = open("11004_K번째 수.txt", "rt")


def solution(N, K, A):
    return sorted(A)[K-1]


if __name__ == "__main__":
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solution(N, K, A))
