def solution(storey):
    digits = list(map(int, str(storey)))
    answer = float('inf')
    stack = [[digits, 0]]
    while stack:
        curr_digits, curr_count = stack.pop()

        if not curr_digits:
            answer = min(answer, curr_count)
            continue

        curr_last_digit = curr_digits.pop()
        stack.append([curr_digits, curr_count + curr_last_digit])

        if curr_digits:
            tmp_digits = curr_digits.copy()
            tmp_digits[-1] += 1
            stack.append([tmp_digits, curr_count + (10 - curr_last_digit)])
        else:
            answer = min(answer, curr_count + (10 - curr_last_digit) + 1)

    return answer


if __name__ == "__main__":
    storey = 56
    print(solution(storey))  # 16