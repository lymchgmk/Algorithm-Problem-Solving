POS_INF = float('inf')
NEG_INF = float('-inf')


def solution(arr):
    nums, ops = [], []
    for idx, element in enumerate(arr):
        nums.append(int(element)) if idx % 2 == 0 else ops.append(element)

    N = len(nums)
    dp_max = [[NEG_INF] * N for _ in range(N)]
    dp_min = [[POS_INF] * N for _ in range(N)]
    for scope in range(N):
        for start in range(N - scope):
            end = start + scope
            if start == end:
                dp_max[start][start] = dp_min[start][start] = nums[start]
                continue

            for mid in range(start, end):
                print(start, mid, end)
                if ops[mid] == '+':
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][mid] + dp_max[mid + 1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][mid] + dp_min[mid + 1][end])
                elif ops[mid] == '-':
                    dp_max[start][end] = max(dp_max[start][end], dp_max[start][mid] - dp_min[mid + 1][end])
                    dp_min[start][end] = min(dp_min[start][end], dp_min[start][mid] - dp_max[mid + 1][end])

    return dp_max[0][-1]


if __name__ == "__main__":
    arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
    result = 3
    answer = solution(arr)
    print(answer == result, answer)