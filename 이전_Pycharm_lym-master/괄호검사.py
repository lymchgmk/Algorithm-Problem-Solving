import sys
sys.stdin = open("괄호검사.txt", "r")

T = int(input())

brkt_left = ["(", "{"]
brkt_right = [")", "}"]

parentheses = ["(", ")"]
curly_brkt = ["{", "}"]

for test_case in range(1, T + 1):
    input_str = input()

    L = len(input_str)
    stack = []

    for i in range(L):
        if input_str[i] in brkt_left:
            stack.append(input_str[i])

        elif input_str[i] in brkt_right:

            if len(stack) == 0:
                stack.append(input_str[i])
                break
            elif ((input_str[i] in parentheses) and (stack[-1] in parentheses)) or ((input_str[i] in curly_brkt) and (stack[-1] in curly_brkt)):
                stack.pop()
            else:
                stack.append(input_str[i])
                break

    if len(stack) == 0:
        print("#{} 1".format(test_case))
    else:
        print("#{} 0".format(test_case))