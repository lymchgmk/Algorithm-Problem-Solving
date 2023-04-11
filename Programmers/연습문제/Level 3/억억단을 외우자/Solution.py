from collections import defaultdict


def solution(e, starts):
    dp = [0] * (e + 1)

    starts.sort()

    for s in starts:
        print(s, get_count(s))

def get_count(num):
    count = 0

    for div in range(1, int(num ** 0.5) + 1):
        q, r = divmod(num, div)

        if r == 0:
            if div == q:
                count += 1
            else:
                count += 2

    return count


if __name__ == "__main__":
    e = 8
    starts = [1, 3, 7]
    result = [6, 6, 8]
    answer = solution(e, starts)
    print([result == answer], answer)
