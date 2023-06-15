def solution(s):

    def expand(left: int, right: int) -> str:
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left: right + 1]

    if len(s) == 1 or s == s[::-1]:
        return len(s)

    result = ""
    for i in range(len(s) - 1):
        result = max(result, expand(i, i), expand(i, i+1), key=len)

    return len(result)


if __name__ == "__main__":
    s = "abcdcba"
    result = 7
    answer = solution(s)
    print(result == answer, answer)
