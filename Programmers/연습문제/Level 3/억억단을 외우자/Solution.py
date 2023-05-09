from math import sqrt


def solution(e, starts):
    dp_count = [0] * (e + 1)
    for div in range(2, e + 1):
        for q in range(1, min(e // div + 1, div)):
            dp_count[div * q] += 2
    for root in range(1, int(sqrt(e))+1):
        dp_count[root ** 2] += 1

    dp_div = [0] * (e + 1)
    max_count = 0
    for idx in range(e, 0, -1):
        if max_count <= dp_count[idx]:
            max_count = dp_count[idx]
            dp_div[idx] = idx
        else:
            dp_div[idx] = dp_div[idx + 1]

    return [dp_div[start] for start in starts]


if __name__ == "__main__":
    e = 8
    starts = [1, 3, 7]
    result = [6, 6, 8]
    answer = solution(e, starts)
    print([result == answer], answer)
