NEG_INF = float('-inf')
POS_INF = float('inf')


def solution(arr):
    nums, ops = [], []
    for idx, element in enumerate(arr):
        nums.append(element) if not idx % 2 else ops.append(element)

    N = len(nums)
    dp_max = [[NEG_INF] * N for _ in range(N)]
    dp_min = [[POS_INF] * N for _ in range(N)]

    for scope in range(N):
        for start in range(N - scope):
            end = start + scope
            if start == end:
                dp_max[start][start] = dp_min[start][start] = int(nums[start])
                continue

            for mid in range(start, end):
                if ops[mid] == '+':
                    dp_max[start][end] = max(dp_max[start][mid] + dp_max[mid + 1][end], dp_max[start][end])
                    dp_min[start][end] = min(dp_min[start][mid] + dp_min[mid + 1][end], dp_min[start][end])
                elif ops[mid] == '-':
                    dp_max[start][end] = max(dp_max[start][mid] - dp_min[mid + 1][end], dp_max[start][end])
                    dp_min[start][end] = min(dp_min[start][mid] - dp_max[mid + 1][end], dp_min[start][end])

    return dp_max[0][N - 1]


if __name__ == "__main__":
    arr = ["1", "-", "3", "+", "5", "-", "8"]
    result = 1
    answer = solution(arr)
    print(answer == result, answer)