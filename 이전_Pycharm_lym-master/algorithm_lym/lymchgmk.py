# def move2048(line):
#     L = len(line)
#     stack = []
#     stack.append(line.pop(0))
#
#     count = 0
#     while line:
#         print(count, "line", line)
#         print(count, "stack", stack)
#         count += 1
#
#         if stack[-1] == 0:
#             stack.pop(-1)
#
#         if stack[-1] == line[0]:
#             stack[-1] = stack[-1] + line.pop(0)
#
#         else:
#             stack.append(line.pop(0))
#
#
#
#     if len(stack) != L:
#         stack += [0]*(L-len(stack))
#
#     return stack


def move2048(line):
    L = len(line)
    stack = []
    stack.append(line.pop(0))
    result = []


    count = 0
    while line:
        print(count, "line", line)
        print(count, "stack", stack)
        count += 1

        temp = line.pop(0)

        if stack[-1] == temp:
            stack[-1] = 2*temp
            stack.append(line.pop(0))

        else:
            stack.append(temp)

        if stack[-1] == 0:
            stack.pop(-1)

    if len(stack) != L:
        stack += [0] * (L - len(stack))

    return stack

line = [4, 4, 8, 2, 0]
print(move2048(line))
# [8, 8, 2, 0, 0]

