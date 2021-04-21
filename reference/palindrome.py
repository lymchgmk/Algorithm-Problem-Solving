def solution1(s):
    answer = 1
    for left in range(len(s)):
        for right in range(left, len(s)):
            tmp = s[left:right + 1]
            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))
    
    return answer


def solution2(s):
    if len(s) <= 1:
        return s
    i, l = 0, 0
    for j in range(len(s)):
        if s[j - l: j + 1] == s[j - l: j + 1][::-1]:
            i, l = j - l, l + 1
            # print(s[i: i+l])
        elif j - l > 0 and s[j - l - 1: j + 1] == s[j - l - 1: j + 1][::-1]:
            i, l = j - l - 1, l + 2
            # print(s[i: i+l])
    return len(s[i: i + l])