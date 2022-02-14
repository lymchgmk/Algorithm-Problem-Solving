import sys
sys.stdin = open("10971_외판원 순회 2.txt", "rt")


def solution(curr, prev):
    # 방문한 적 있는 경우
    if dp[curr][prev]:
        return dp[curr][prev]
    # 모두 방문한 경우
    if prev == (1 << N) - 1:
        return W[curr][0] if W[curr][0] > 0 else float('inf')
    # 다음으로 갈 곳 탐색
    cost = float('inf')
    for i in range(1, N):
        # curr에서 i로 갈 수 있고, i를 안가본 경우
        if W[curr][i] != 0 and not (prev >> i) % 2:
            # 최소 비용 비교
            cost = min(cost, solution(i, prev | (1 << i)) + W[curr][i])
    # 메모이제이션
    dp[curr][prev] = cost

    return cost


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N)]
    answer = solution(0, 1)
    print(answer)
