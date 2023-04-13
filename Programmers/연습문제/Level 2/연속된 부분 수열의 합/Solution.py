def solution(sequence, k):
    start = end = 0
    partial_sum = 0
    answer = [0, len(sequence) - 1]

    while start < len(sequence) and end < len(sequence):
        while partial_sum < k:
            end += 1
            partial_sum += sequence[end]

        if partial_sum == k:
            print(777, start, end)
            start = end
            partial_sum = sequence[start]

        while k < partial_sum:
            partial_sum -= sequence[start]
            start += 1

        if partial_sum == k:
            print(778, start, end)
            start = end
            partial_sum = sequence[start]

    return answer


if __name__ == "__main__":
    sequence = [1, 1, 1, 2, 3, 4, 5]
    k = 5
    result = [6, 6]
    answer = solution(sequence, k)
    print(f"{answer == result}, {answer}")
