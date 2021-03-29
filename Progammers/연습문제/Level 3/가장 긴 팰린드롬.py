def solution(s):
    answer = 1
    for left in range(len(s)):
        for right in range(left, len(s)):
            tmp = s[left:right+1]
            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))

    return answer


s = "abcdcba"
print(solution(s))
