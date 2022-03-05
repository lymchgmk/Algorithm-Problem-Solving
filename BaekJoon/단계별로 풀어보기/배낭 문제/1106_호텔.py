import sys
sys.stdin = open('1106_호텔.txt', 'rt')


def solution(C, N, CITYS):
    dp = [0] + [float('inf')] * (C + 100)
    for cost, man in CITYS:
        for curr_man in range(man, C + 100):
            dp[curr_man] = min(dp[curr_man], dp[curr_man - man] + cost)
    return min(dp[C:])


if __name__ == "__main__":
    C, N = map(int, input().split())
    CITYS = [map(int, input().split()) for _ in range(N)]
    print(solution(C, N, CITYS))
