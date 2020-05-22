import sys
sys.stdin=open('튜플.txt')

def solution(s):
    answer = []
    sample1 = []
    sample2 = []
    count_s = []

    for char in s:
        if char.isdigit() or char == ",":
            sample1.append(char)

    test1 = ''.join(sample1)
    test2 = test1.split(',')

    for string in test2:
        if int(string) not in sample2:
            sample2.append(int(string))
            count_s.append([s.count(string), int(string)])

    count_s.sort(reverse=True)
    for c in count_s:
        answer.append(c[1])

    return answer

s=input()

print(solution(s))