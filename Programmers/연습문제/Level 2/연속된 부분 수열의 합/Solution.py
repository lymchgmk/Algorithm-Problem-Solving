def solution(sequence, k):
    partial_sum = 0
    right = 0
    result = []
    for left in range(len(sequence)):
        while right < len(sequence) and partial_sum < k:
            partial_sum += sequence[right]
            right += 1

        if partial_sum == k:
            if not result:
                result = [left, right - 1]
            else:
                result = result if result[1] - result[0] <= (right - 1) - left else [left, right - 1]

        partial_sum -= sequence[left]

    return result


if __name__ == "__main__":
    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    result = [6, 6]
    answer = solution(sequence, k)
    print(f"{answer == result}, {answer}")
