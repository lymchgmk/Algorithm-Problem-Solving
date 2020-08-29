def move2048(line):
    L = len(line)
    stack = []
    check = [0]

    while len(line) != 0:
        temp = line.pop(0)

        if temp == 0 and len(line) != 0:
            continue

        elif temp != 0 and len(line) == 0:
            if check[-1] == 0 and stack[-1] == temp:
                stack[-1] = 2*temp
                check.append(1)
            else:
                stack.append(temp)
                check.append(0)
                break

        elif temp != 0 and len(line) != 0:
            if len(stack) == 0:
                stack.append(temp)
                check.append(0)
            else:
                if check[-1] == 0 and stack[-1] == temp:
                    stack[-1] = 2*temp
                    check.append(1)
                else:
                    stack.append(temp)
                    check.append(0)

    if len(stack) != L:
        stack += [0] * (L - len(stack))

    return stack

def move_to_dir(puzzle, S):
    if S == "up":
        temp1 = []
        for i in range(len(puzzle)):
            temp1.append(move2048(column[i]))

        temp2 = []
        for i in range(len(temp1)):
            temp2.append([temp2_row[i] for temp2_row in temp1])

        for i in range(len(temp2)):
            print(*temp2[i])


    elif S == "down":
        temp1 = []
        for i in range(len(puzzle)):
            temp0 = (column[i])[::-1]
            temp1.append(move2048(temp0))

        temp00 = []
        for i in range(len(temp1)):
            temp00.append((temp1[i])[::-1])

        temp2 = []
        for i in range(len(temp00)):
            temp2.append([temp2_row[i] for temp2_row in temp00])

        for i in range(len(temp2)):
            print(*temp2[i])


    elif S == "left":
        temp1 = []
        for i in range(len(puzzle)):
            temp1.append(move2048(row[i]))

        for i in range(len(temp1)):
            print(*temp1[i])


    elif S == "right":
        temp1 = []
        for i in range(len(puzzle)):
            temp1.append(move2048(row[i][::-1]))

        for i in range(len(temp1)):
            print(*temp1[i][::-1])



N = int(input())

puzzle = [list(map(int, input().split())) for _ in range(N)]

row = []
column = []
for i in range(len(puzzle)):
    row.append(puzzle[i])
    column.append([r[i] for r in puzzle])


