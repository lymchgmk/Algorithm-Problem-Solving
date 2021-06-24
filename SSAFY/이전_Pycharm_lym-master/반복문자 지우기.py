import sys
sys.stdin = open("반복문자 지우기.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    input_str = list(input())

    stack = []

    while input_str:
        if len(stack) == 0:
            stack.append(input_str.pop(0))
        if len(input_str) != 0:
            temp = input_str.pop(0)
            if temp == stack[-1]:
                stack.pop()
            else:
                stack.append(temp)
        else:
            break

    print("#{} {}".format(test_case, len(stack)))