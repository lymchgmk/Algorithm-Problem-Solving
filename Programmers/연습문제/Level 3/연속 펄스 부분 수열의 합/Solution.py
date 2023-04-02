def solution(sequence):
    first, second = [], []

    for idx, number in enumerate(sequence):
        first.append(number * (1 if idx % 2 else -1))
        second.append(number * (-1 if idx % 2 else 1))

    max_first = dynamic_programming(first)
    max_second = dynamic_programming(second)

    return max(max_first, max_second)


def dynamic_programming(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]

    for i in range(1, len(arr)):
        dp[i] = max(0, dp[i-1]) + arr[i]

    return max(dp)


if __name__ == "__main__":
    sequence = [2, 3, -6, 1, 3, -1, 2, 4]
    result = 10
    answer = solution(sequence)
    print([result == answer], answer)
