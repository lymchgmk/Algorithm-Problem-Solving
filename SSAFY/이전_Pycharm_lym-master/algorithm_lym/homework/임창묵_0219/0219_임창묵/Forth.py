import sys
sys.stdin = open('Forth.txt', 'r')

def calculate(n1, n2, c):
    if c == "+":
        return n1+n2
    elif c == "-":
        return n1-n2
    elif c == "*":
        return n1*n2
    elif c == "/":
        return n1//n2

def Forth(str):
    count_digit = 0
    count_else = 0
    for char in str:
        if char.isdigit():
            count_digit += 1
        else:
            count_else += 1

    if count_digit != count_else:
        return 'error'

    stack = []
    while str:
        char = str.pop(0)

        if char == '.':
            return stack[0]

        elif char.isdigit():
            stack.append(int(char))

        else:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(calculate(num1, num2, char))


T = int(input())

for test_case in range(1, T+1):
    data = list(input().split())

    print("#{} {}".format(test_case, Forth(data)))