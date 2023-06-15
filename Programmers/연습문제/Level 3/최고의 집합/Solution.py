def solution(n, s):
    if s < n:
        return [-1]

    q, r = divmod(s, n)
    return [q] * (n - r) + [q+1] * r


if __name__ == "__main__":
    n = 2
    s = 9
    result = [4, 5]
    answer = solution(n, s)
    print(answer == result, answer)
