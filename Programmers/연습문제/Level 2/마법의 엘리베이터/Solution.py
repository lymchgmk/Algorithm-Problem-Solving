def solution(storey):
    digits = list(map(int, str(storey)))
    answer = storey
    queue = [[digits, 0]]
    while queue:
        curr_digits, curr_count = queue.pop()

        if not curr_digits:
            answer = min(answer, curr_count)
            continue

        curr_last_digit = curr_digits.pop()
        queue.append([curr_digits, curr_count + curr_last_digit])

        if curr_digits:
            post_digits = curr_digits.copy()
            post_digits[-1] += 1
            queue.append([post_digits, curr_count + (10 - curr_last_digit)])
        else:
            answer = min(answer, curr_count + (10 - curr_last_digit) + 1)

    return answer


if __name__ == "__main__":
    storey = 2554
    print(solution(storey))  # 16