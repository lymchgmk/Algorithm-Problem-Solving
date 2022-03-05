import sys
sys.stdin = open('2662_기업투자.txt', 'rt')


def solution(N, M, C):
    dp = [[[0]*(M+1) for _ in range(N+1)] for _ in range(M+1)]
    for i in range(1, N+1):
        money, *firms = C[i-1]
        for j in range(1, M+1):



if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    C = [map(int, input().split()) for _ in range(N)]
    print(solution(N, M, CAB))
