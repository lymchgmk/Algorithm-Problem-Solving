def make_row(target, n):
    return [target]*(target) + list(range(target+1, n+1))


def solution(n, left, right):
    left_row, left_col = divmod(left, n)
    right_row, right_col = divmod(right, n)

    arr = [make_row(r, n) for r in range(left_row+1, right_row+2)]

    start = left_col
    end = n*(right_row-left_row) + right_col
    return arr[start:end+1]


if __name__ == "__main__":
    # tc 1
    n = 3
    left = 2
    right = 5
    print(solution(n, left, right))

    # tc 2
    n = 4
    left = 7
    right = 14
    print(solution(n, left, right))
