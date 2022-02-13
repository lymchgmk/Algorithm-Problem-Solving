import sys
sys.stdin = open("10799_쇠막대기.txt", "rt")


def solution(str):
    answer = 0
    stack = []
    check = ''
    for char in str:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
                if check == '(':
                    answer += len(stack)
                else:
                    answer += 1
        check = char

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    str = list(input())
    print(solution(str))
