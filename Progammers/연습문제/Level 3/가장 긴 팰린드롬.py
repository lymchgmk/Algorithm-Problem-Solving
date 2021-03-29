def solution(s):
    answer = 1
    for left in range(len(s)):
        for right in range(left, len(s)):
            tmp = s[left:right+1]
            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))

    return answer


def solution_2(s):
    return len(s) if s == s[::-1] else max(solution_2(s[1:]), solution_2(s[:-1]))


s = "abcdcba"
print(solution(s))
