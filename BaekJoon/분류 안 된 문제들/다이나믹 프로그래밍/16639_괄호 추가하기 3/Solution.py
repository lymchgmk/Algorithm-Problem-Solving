import sys
sys.stdin = open("input.txt", "rt")


POS_INF = float('inf')
NEG_INF = float('-inf')


def solution(N, exp):
    nums, ops = [], []
    for idx, element in enumerate(exp):
        nums.append(int(element)) if idx % 2 == 0 else ops.append(element)

    L = len(nums)
    dp_max = [[NEG_INF] * L for _ in range(L)]
    dp_min = [[POS_INF] * L for _ in range(L)]
    for scope in range(L):
        for start in range(L - scope):
            end = start + scope

            if start == end:
                dp_max[start][start] = dp_min[start][start] = nums[start]
                continue

            for mid in range(start, end):
                if ops[mid] == '+':
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][mid] + dp_max[mid + 1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][mid] + dp_min[mid + 1][end])
                elif ops[mid] == '-':
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][mid] - dp_min[mid + 1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][mid] - dp_max[mid + 1][end])
                elif ops[mid] == '*':
                    dp_max[start][end] = max(dp_max[start][end],
                                             dp_max[start][mid] * dp_max[mid + 1][end],
                                             dp_max[start][mid] * dp_min[mid + 1][end],
                                             dp_min[start][mid] * dp_max[mid + 1][end],
                                             dp_min[start][mid] * dp_min[mid + 1][end])
                    dp_min[start][end] = min(dp_min[start][end],
                                             dp_max[start][mid] * dp_max[mid + 1][end],
                                             dp_max[start][mid] * dp_min[mid + 1][end],
                                             dp_min[start][mid] * dp_max[mid + 1][end],
                                             dp_min[start][mid] * dp_min[mid + 1][end])

    return dp_max[0][-1]


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    exp = input()
    result = 136
    answer = solution(N, exp)
    print(answer == result, answer)

