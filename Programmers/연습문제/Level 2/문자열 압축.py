import re


def solution(s):
    answer = len(s)
    for L in range(1, len(s)//2+1):
        pattern = '\w{'+ str(L) + '}'
        regex = re.findall(pattern, s)
        if L * len(regex) != len(s):
            regex.append(s[L*len(regex):])

        zipped_s = ''
        cur_word = regex[0]
        cur_cnt = 1
        for a, b in zip(regex, regex[1:] + ['']):
            if a == b:
                cur_cnt += 1
            else:
                if cur_cnt != 1:
                    zipped_s += str(cur_cnt)
                zipped_s += cur_word
                cur_word = b
                cur_cnt = 1
        
        answer = min(answer, len(zipped_s))

    return answer


s = "abcabcdede"
print(solution(s))
