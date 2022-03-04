import sys
sys.stdin = open('2504_괄호의 값.txt', 'rt')


def solution(S):
    check = {')': '(', ']': '['}
    num = {')': 2, ']': 3}
    stack = []
    ans = 0
    tmp = 0
    for s in S:
        if s in ('(', '['):
            stack.append(s)
        else:
            if not stack:
                return 0
            last = stack.pop()
            if last.isdigit():
                tmp += int(last)
            else:
                stack.append(num[last])





if __name__ == "__main__":
    input = sys.stdin.readline
    S = list(input())
    print(solution(S))
