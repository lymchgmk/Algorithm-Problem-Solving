import re


def solution(dartResult):
    darts = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    answer = [0]*len(darts)
    for i in range(len(darts)):
        num, bonus, option = darts[i]
        answer[i] += int(num)
        if bonus == 'D':
            answer[i] **= 2
        elif bonus == 'T':
            answer[i] **= 3
        if option == '#':
            answer[i] *= -1
        elif option == '*':
            answer[i] *= 2
            if i:
                answer[i-1] *= 2

    return sum(answer)


dartResult = '1D2S#10S'
print(solution(dartResult))