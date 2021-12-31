import sys
sys.stdin = open("4949_균형잡힌 세상.txt", "rt")


while True:
    stack = []
    flag = True
    line = list(input())
    if line == ["."]:
        break

    for c in line:
        if c == "(" or c == "[":
            stack.append(c)

        elif c == ")" or c == "]":
            if not stack:
                flag = False
                break
            else:
                temp = stack.pop()
                if (c ==")" and temp != "(") or (c =="]" and temp != "["):
                    flag = False
                    break
    
    if not stack and flag == True:
        print("yes")
    else:
        print("no")